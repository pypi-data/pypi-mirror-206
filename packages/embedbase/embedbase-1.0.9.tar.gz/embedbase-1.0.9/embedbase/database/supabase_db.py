import asyncio
from typing import Coroutine, List, Optional
from pandas import DataFrame, Series
from embedbase.database import VectorDatabase
from embedbase.utils import BatchGenerator


class Supabase(VectorDatabase):
    def __init__(self, url: str, key: str, **kwargs):
        """
        :param url: supabase url
        :param key: supabase key
        """
        super().__init__(**kwargs)
        try:
            from supabase import create_client, Client

            self.supabase: Client = create_client(url, key)
            self.functions = self.supabase.functions()

        except ImportError:
            raise ImportError("Please install supabase with `pip install supabase`")

    async def select(
        self,
        ids: List[str] = [],
        hashes: List[str] = [],
        dataset_id: Optional[str] = None,
        user_id: Optional[str] = None,
        distinct: bool = True,
    ) -> List[dict]:
        # either ids or hashes must be provided
        assert ids or hashes, "ids or hashes must be provided"

        req = self.supabase.table("documents").select("*")
        if ids:
            req = req.in_("id", ids)
            if distinct:
                # hack: supabase does not support distinct
                req = req.order("id", desc=True)
                req = req.limit(len(ids))
        if hashes:
            req = req.in_("hash", hashes)
            if distinct:
                # hack: supabase does not support distinct
                req = req.order("hash", desc=True)
                req = req.limit(len(hashes))
        if dataset_id:
            req = req.eq("dataset_id", dataset_id)
        if user_id:
            req = req.eq("user_id", user_id)
        
        return req.execute().data

    async def update(
        self,
        df: DataFrame,
        dataset_id: str,
        user_id: Optional[str] = None,
        batch_size: Optional[int] = 100,
        store_data: bool = True,
    ) -> Coroutine:
        df_batcher = BatchGenerator(batch_size)
        batches = [batch_df for batch_df in df_batcher(df)]

        async def _insert(batch_df: DataFrame):
            def _d(row: Series):
                data = {
                    "id": row.id,
                    "embedding": row.embedding,
                    "hash": row.hash,
                    "dataset_id": dataset_id,
                    "user_id": user_id,
                    "metadata": row.metadata,
                }
                if store_data:
                    data["data"] = row.data
                return data

            response = (
                self.supabase.table("documents")
                .upsert([_d(row) for _, row in batch_df.iterrows()])
                .execute()
            )
            return response

        # TODO: not sure truly parallel, python garbage
        results = await asyncio.gather(*[_insert(batch_df) for batch_df in batches])
        return results

    async def delete(
        self,
        ids: List[str],
        dataset_id: str,
        user_id: Optional[str] = None,
    ) -> None:
        req = self.supabase.table("documents").delete().eq("dataset_id", dataset_id)
        if user_id:
            req = req.eq("user_id", user_id)
        return req.in_("id", ids).execute()

    async def search(
        self,
        vector: List[float],
        top_k: Optional[int],
        dataset_ids: List[str],
        user_id: Optional[str] = None,
    ) -> List[dict]:
        d = {
            "query_embedding": vector,
            "similarity_threshold": 0.1,  # TODO: make this configurable
            "match_count": top_k,
            "query_dataset_ids": dataset_ids,
        }
        if user_id:
            d["query_user_id"] = user_id
        return (
            self.supabase.rpc(
                "match_documents",
                d,
            )
            .execute()
            .data
        )

    async def clear(self, dataset_id: str, user_id: Optional[str] = None) -> None:
        req = self.supabase.table("documents").delete().eq("dataset_id", dataset_id)
        if user_id:
            req = req.eq("user_id", user_id)
        return req.execute()

    async def get_datasets(self, user_id: Optional[str] = None) -> List[dict]:
        req = self.supabase.table("distinct_datasets").select(
            "dataset_id", "documents_count"
        )
        if user_id:
            req = req.eq("user_id", user_id)
        data = req.execute().data
        return data
