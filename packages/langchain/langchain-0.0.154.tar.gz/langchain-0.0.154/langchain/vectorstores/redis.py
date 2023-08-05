"""Wrapper around Redis vector database."""
from __future__ import annotations

import json
import logging
import uuid
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Type,
)

import numpy as np
from pydantic import BaseModel, root_validator

from langchain.docstore.document import Document
from langchain.embeddings.base import Embeddings
from langchain.schema import BaseRetriever
from langchain.utils import get_from_dict_or_env
from langchain.vectorstores.base import VectorStore

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from redis.client import Redis as RedisType
    from redis.commands.search.query import Query


# required modules
REDIS_REQUIRED_MODULES = [
    {"name": "search", "ver": 20400},
    {"name": "searchlight", "ver": 20400},
]


def _check_redis_module_exist(client: RedisType, required_modules: List[dict]) -> None:
    """Check if the correct Redis modules are installed."""
    installed_modules = client.module_list()
    installed_modules = {
        module[b"name"].decode("utf-8"): module for module in installed_modules
    }
    for module in required_modules:
        if module["name"] in installed_modules and int(
            installed_modules[module["name"]][b"ver"]
        ) >= int(module["ver"]):
            return
    # otherwise raise error
    error_message = (
        "You must add the RediSearch (>= 2.4) module from Redis Stack. "
        "Please refer to Redis Stack docs: https://redis.io/docs/stack/"
    )
    logging.error(error_message)
    raise ValueError(error_message)


def _check_index_exists(client: RedisType, index_name: str) -> bool:
    """Check if Redis index exists."""
    try:
        client.ft(index_name).info()
    except:  # noqa: E722
        logger.info("Index does not exist")
        return False
    logger.info("Index already exists")
    return True


def _redis_key(prefix: str) -> str:
    """Redis key schema for a given prefix."""
    return f"{prefix}:{uuid.uuid4().hex}"


def _redis_prefix(index_name: str) -> str:
    """Redis key prefix for a given index."""
    return f"doc:{index_name}"


class Redis(VectorStore):
    """Wrapper around Redis vector database.

    To use, you should have the ``redis`` python package installed.

    Example:
        .. code-block:: python

            from langchain.vectorstores import Redis
            from langchain.embeddings import OpenAIEmbeddings

            embeddings = OpenAIEmbeddings()
            vectorstore = Redis(
                redis_url="redis://username:password@localhost:6379"
                index_name="my-index",
                embedding_function=embeddings.embed_query,
            )
    """

    def __init__(
        self,
        redis_url: str,
        index_name: str,
        embedding_function: Callable,
        content_key: str = "content",
        metadata_key: str = "metadata",
        vector_key: str = "content_vector",
        **kwargs: Any,
    ):
        """Initialize with necessary components."""
        try:
            import redis
        except ImportError:
            raise ValueError(
                "Could not import redis python package. "
                "Please install it with `pip install redis`."
            )

        self.embedding_function = embedding_function
        self.index_name = index_name
        try:
            # connect to redis from url
            redis_client = redis.from_url(redis_url, **kwargs)
            # check if redis has redisearch module installed
            _check_redis_module_exist(redis_client, REDIS_REQUIRED_MODULES)
        except ValueError as e:
            raise ValueError(f"Redis failed to connect: {e}")

        self.client = redis_client
        self.content_key = content_key
        self.metadata_key = metadata_key
        self.vector_key = vector_key

    def _create_index(self, dim: int = 1536) -> None:
        try:
            from redis.commands.search.field import TextField, VectorField
            from redis.commands.search.indexDefinition import IndexDefinition, IndexType
        except ImportError:
            raise ValueError(
                "Could not import redis python package. "
                "Please install it with `pip install redis`."
            )

        # Check if index exists
        if not _check_index_exists(self.client, self.index_name):
            # Constants
            distance_metric = (
                "COSINE"  # distance metric for the vectors (ex. COSINE, IP, L2)
            )
            schema = (
                TextField(name=self.content_key),
                TextField(name=self.metadata_key),
                VectorField(
                    self.vector_key,
                    "FLAT",
                    {
                        "TYPE": "FLOAT32",
                        "DIM": dim,
                        "DISTANCE_METRIC": distance_metric,
                    },
                ),
            )
            prefix = _redis_prefix(self.index_name)

            # Create Redis Index
            self.client.ft(self.index_name).create_index(
                fields=schema,
                definition=IndexDefinition(prefix=[prefix], index_type=IndexType.HASH),
            )

    def add_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        embeddings: Optional[List[List[float]]] = None,
        keys: Optional[List[str]] = None,
        batch_size: int = 1000,
        **kwargs: Any,
    ) -> List[str]:
        """Add more texts to the vectorstore.

        Args:
            texts (Iterable[str]): Iterable of strings/text to add to the vectorstore.
            metadatas (Optional[List[dict]], optional): Optional list of metadatas.
                Defaults to None.
            embeddings (Optional[List[List[float]]], optional): Optional pre-generated
                embeddings. Defaults to None.
            keys (Optional[List[str]], optional): Optional key values to use as ids.
                Defaults to None.
            batch_size (int, optional): Batch size to use for writes. Defaults to 1000.

        Returns:
            List[str]: List of ids added to the vectorstore
        """
        ids = []
        prefix = _redis_prefix(self.index_name)

        # Write data to redis
        pipeline = self.client.pipeline(transaction=False)
        for i, text in enumerate(texts):
            # Use provided values by default or fallback
            key = keys[i] if keys else _redis_key(prefix)
            metadata = metadatas[i] if metadatas else {}
            embedding = embeddings[i] if embeddings else self.embedding_function(text)
            pipeline.hset(
                key,
                mapping={
                    self.content_key: text,
                    self.vector_key: np.array(embedding, dtype=np.float32).tobytes(),
                    self.metadata_key: json.dumps(metadata),
                },
            )
            ids.append(key)

            # Write batch
            if i % batch_size == 0:
                pipeline.execute()

        # Cleanup final batch
        pipeline.execute()
        return ids

    def similarity_search(
        self, query: str, k: int = 4, **kwargs: Any
    ) -> List[Document]:
        """
        Returns the most similar indexed documents to the query text.

        Args:
            query (str): The query text for which to find similar documents.
            k (int): The number of documents to return. Default is 4.

        Returns:
            List[Document]: A list of documents that are most similar to the query text.
        """
        docs_and_scores = self.similarity_search_with_score(query, k=k)
        return [doc for doc, _ in docs_and_scores]

    def similarity_search_limit_score(
        self, query: str, k: int = 4, score_threshold: float = 0.2, **kwargs: Any
    ) -> List[Document]:
        """
        Returns the most similar indexed documents to the query text within the
        score_threshold range.

        Args:
            query (str): The query text for which to find similar documents.
            k (int): The number of documents to return. Default is 4.
            score_threshold (float): The minimum matching score required for a document
            to be considered a match. Defaults to 0.2.
            Because the similarity calculation algorithm is based on cosine similarity,
            the smaller the angle, the higher the similarity.

        Returns:
            List[Document]: A list of documents that are most similar to the query text,
            including the match score for each document.

        Note:
            If there are no documents that satisfy the score_threshold value,
            an empty list is returned.

        """
        docs_and_scores = self.similarity_search_with_score(query, k=k)
        return [doc for doc, score in docs_and_scores if score < score_threshold]

    def _prepare_query(self, k: int) -> Query:
        try:
            from redis.commands.search.query import Query
        except ImportError:
            raise ValueError(
                "Could not import redis python package. "
                "Please install it with `pip install redis`."
            )
        # Prepare the Query
        hybrid_fields = "*"
        base_query = (
            f"{hybrid_fields}=>[KNN {k} @{self.vector_key} $vector AS vector_score]"
        )
        return_fields = [self.metadata_key, self.content_key, "vector_score"]
        return (
            Query(base_query)
            .return_fields(*return_fields)
            .sort_by("vector_score")
            .paging(0, k)
            .dialect(2)
        )

    def similarity_search_with_score(
        self, query: str, k: int = 4
    ) -> List[Tuple[Document, float]]:
        """Return docs most similar to query.

        Args:
            query: Text to look up documents similar to.
            k: Number of Documents to return. Defaults to 4.

        Returns:
            List of Documents most similar to the query and score for each
        """
        # Creates embedding vector from user query
        embedding = self.embedding_function(query)

        # Creates Redis query
        redis_query = self._prepare_query(k)

        params_dict: Mapping[str, str] = {
            "vector": np.array(embedding)  # type: ignore
            .astype(dtype=np.float32)
            .tobytes()
        }

        # Perform vector search
        results = self.client.ft(self.index_name).search(redis_query, params_dict)

        # Prepare document results
        docs = [
            (
                Document(
                    page_content=result.content, metadata=json.loads(result.metadata)
                ),
                float(result.vector_score),
            )
            for result in results.docs
        ]

        return docs

    @classmethod
    def from_texts(
        cls: Type[Redis],
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        index_name: Optional[str] = None,
        content_key: str = "content",
        metadata_key: str = "metadata",
        vector_key: str = "content_vector",
        **kwargs: Any,
    ) -> Redis:
        """Create a Redis vectorstore from raw documents.
        This is a user-friendly interface that:
            1. Embeds documents.
            2. Creates a new index for the embeddings in Redis.
            3. Adds the documents to the newly created Redis index.
        This is intended to be a quick way to get started.
        Example:
            .. code-block:: python
                from langchain.vectorstores import Redis
                from langchain.embeddings import OpenAIEmbeddings
                embeddings = OpenAIEmbeddings()
                redisearch = RediSearch.from_texts(
                    texts,
                    embeddings,
                    redis_url="redis://username:password@localhost:6379"
                )
        """
        redis_url = get_from_dict_or_env(kwargs, "redis_url", "REDIS_URL")

        if "redis_url" in kwargs:
            kwargs.pop("redis_url")

        # Name of the search index if not given
        if not index_name:
            index_name = uuid.uuid4().hex

        # Create instance
        instance = cls(
            redis_url=redis_url,
            index_name=index_name,
            embedding_function=embedding.embed_query,
            content_key=content_key,
            metadata_key=metadata_key,
            vector_key=vector_key,
            **kwargs,
        )

        # Create embeddings over documents
        embeddings = embedding.embed_documents(texts)

        # Create the search index
        instance._create_index(dim=len(embeddings[0]))

        # Add data to Redis
        instance.add_texts(texts, metadatas, embeddings)
        return instance

    @staticmethod
    def drop_index(
        index_name: str,
        delete_documents: bool,
        **kwargs: Any,
    ) -> bool:
        """
        Drop a Redis search index.

        Args:
            index_name (str): Name of the index to drop.
            delete_documents (bool): Whether to drop the associated documents.

        Returns:
            bool: Whether or not the drop was successful.
        """
        redis_url = get_from_dict_or_env(kwargs, "redis_url", "REDIS_URL")
        try:
            import redis
        except ImportError:
            raise ValueError(
                "Could not import redis python package. "
                "Please install it with `pip install redis`."
            )
        try:
            # We need to first remove redis_url from kwargs,
            # otherwise passing it to Redis will result in an error.
            if "redis_url" in kwargs:
                kwargs.pop("redis_url")
            client = redis.from_url(url=redis_url, **kwargs)
        except ValueError as e:
            raise ValueError(f"Your redis connected error: {e}")
        # Check if index exists
        try:
            client.ft(index_name).dropindex(delete_documents)
            logger.info("Drop index")
            return True
        except:  # noqa: E722
            # Index not exist
            return False

    @classmethod
    def from_existing_index(
        cls,
        embedding: Embeddings,
        index_name: str,
        content_key: str = "content",
        metadata_key: str = "metadata",
        vector_key: str = "content_vector",
        **kwargs: Any,
    ) -> Redis:
        """Connect to an existing Redis index."""
        redis_url = get_from_dict_or_env(kwargs, "redis_url", "REDIS_URL")
        try:
            import redis
        except ImportError:
            raise ValueError(
                "Could not import redis python package. "
                "Please install it with `pip install redis`."
            )
        try:
            # We need to first remove redis_url from kwargs,
            # otherwise passing it to Redis will result in an error.
            if "redis_url" in kwargs:
                kwargs.pop("redis_url")
            client = redis.from_url(url=redis_url, **kwargs)
            # check if redis has redisearch module installed
            _check_redis_module_exist(client, REDIS_REQUIRED_MODULES)
            # ensure that the index already exists
            assert _check_index_exists(
                client, index_name
            ), f"Index {index_name} does not exist"
        except Exception as e:
            raise ValueError(f"Redis failed to connect: {e}")

        return cls(
            redis_url,
            index_name,
            embedding.embed_query,
            content_key=content_key,
            metadata_key=metadata_key,
            vector_key=vector_key,
            **kwargs,
        )

    def as_retriever(self, **kwargs: Any) -> BaseRetriever:
        return RedisVectorStoreRetriever(vectorstore=self, **kwargs)


class RedisVectorStoreRetriever(BaseRetriever, BaseModel):
    vectorstore: Redis
    search_type: str = "similarity"
    k: int = 4
    score_threshold: float = 0.4

    class Config:
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    @root_validator()
    def validate_search_type(cls, values: Dict) -> Dict:
        """Validate search type."""
        if "search_type" in values:
            search_type = values["search_type"]
            if search_type not in ("similarity", "similarity_limit"):
                raise ValueError(f"search_type of {search_type} not allowed.")
        return values

    def get_relevant_documents(self, query: str) -> List[Document]:
        if self.search_type == "similarity":
            docs = self.vectorstore.similarity_search(query, k=self.k)
        elif self.search_type == "similarity_limit":
            docs = self.vectorstore.similarity_search_limit_score(
                query, k=self.k, score_threshold=self.score_threshold
            )
        else:
            raise ValueError(f"search_type of {self.search_type} not allowed.")
        return docs

    async def aget_relevant_documents(self, query: str) -> List[Document]:
        raise NotImplementedError("RedisVectorStoreRetriever does not support async")

    def add_documents(self, documents: List[Document], **kwargs: Any) -> List[str]:
        """Add documents to vectorstore."""
        return self.vectorstore.add_documents(documents, **kwargs)

    async def aadd_documents(
        self, documents: List[Document], **kwargs: Any
    ) -> List[str]:
        """Add documents to vectorstore."""
        return await self.vectorstore.aadd_documents(documents, **kwargs)
