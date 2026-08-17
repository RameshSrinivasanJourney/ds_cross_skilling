from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PayloadSchemaType

from app.core.config import settings
from app.utils.logger import logger

from qdrant_client.models import PointStruct
from app.data.employee_documents import EMPLOYEE_DOCUMENTS
from app.services.embedding_service import EmbeddingService

from qdrant_client.models import (

    Filter,

    FieldCondition,

    MatchValue

)


class QdrantService:

    def __init__(self):

        logger.info(

            "Initializing Qdrant..."

        )

        self.client = QdrantClient(

            url=settings.QDRANT_URL,

            api_key=settings.QDRANT_API_KEY

        )

        logger.info(

            "Qdrant Connected Successfully."

        )

    # ==========================================================
    # Qdrant - Health
    # ==========================================================

    def health(self):

        logger.info(

            "Checking Qdrant Health..."

        )

        collections = self.client.get_collections()

        total_collections = len(

            collections.collections

        )

        logger.info(

            "Qdrant Health Check Completed."

        )

        return {

            "status": "Success",

            "message": "Qdrant Connected Successfully.",

            "total_collections": total_collections

        }

    # ==========================================================
    # Qdrant - Collections
    # ==========================================================

    def create_collection(

        self,

        collection_name: str,

        vector_size: int,

        distance: str

    ):

        logger.info(

            f"Creating Collection : {collection_name}"

        )

        distance_map = {

            "Cosine": Distance.COSINE,

            "Dot": Distance.DOT,

            "Euclid": Distance.EUCLID

        }

        try:

            self.client.create_collection(

                collection_name=collection_name,

                vectors_config=VectorParams(

                    size=vector_size,

                    distance=distance_map.get(

                        distance,

                        Distance.COSINE

                    )

                )

            )
            # =============================================
            #Qdrant Cloud requires a payload index before you can filter on payload fields like:
            # department
            # category
            # Unlike ChromaDB, Qdrant Cloud does not automatically create payload indexes.
            # After creating the collection, create indexes for the payload fields.
            # =============================================
            self.client.create_payload_index(
                collection_name=collection_name,
                field_name="department",
                field_schema=PayloadSchemaType.KEYWORD
            )

            self.client.create_payload_index(
                collection_name=collection_name,
                field_name="category",
                field_schema=PayloadSchemaType.KEYWORD
            )

        except Exception as ex:

            logger.error(str(ex))

            return {

                "status": "Failed",

                "collection_name": collection_name,

                "vector_size": vector_size,

                "distance": distance,

                "message": str(ex)

            }

        logger.info(

            "Collection Created Successfully."

        )

        return {

            "status": "Success",

            "collection_name": collection_name,

            "vector_size": vector_size,

            "distance": distance,

            "message": "Collection created successfully."

        }

    def list_collections(self):

        logger.info(

            "Fetching Collections..."

        )

        response = self.client.get_collections()

        collections = [

            collection.name

            for collection in response.collections

        ]

        logger.info(

            f"{len(collections)} collections found."

        )

        return {

            "status": "Success",

            "total_collections": len(collections),

            "collections": collections

        }

    def collection_info(

        self,

        collection_name: str

    ):

        logger.info(

            f"Fetching Collection Info : {collection_name}"

        )

        try:

            info = self.client.get_collection(

                collection_name=collection_name

            )

        except Exception:

            return {

                "status": "Failed",

                "collection_name": collection_name,

                "total_points": 0,

                "vector_size": 0

            }

        vectors = info.config.params.vectors

        vector_size = vectors.size

        logger.info(

            "Collection Info Retrieved."

        )

        return {

            "status": "Success",

            "collection_name": collection_name,

            "total_points": info.points_count,

            "vector_size": vector_size

        }

    def delete_collection(

        self,

        collection_name: str

    ):

        logger.info(

            f"Deleting Collection : {collection_name}"

        )

        try:

            self.client.delete_collection(

                collection_name=collection_name

            )

        except Exception:

            return {

                "status": "Failed",

                "message": "Collection not found."

            }

        logger.info(

            "Collection Deleted Successfully."

        )

        return {

            "status": "Success",

            "message": f"{collection_name} deleted successfully."

        }
    
    # ==========================================================
    # Qdrant - Points
    # ==========================================================

    def load_points(

        self,

        collection_name: str

    ):

        logger.info(

            f"Loading Points into Collection : {collection_name}"

        )

        points = []

        for index, document in enumerate(EMPLOYEE_DOCUMENTS):

            embedding = EmbeddingService.generate_embedding(

                document["text"]

            )

            points.append(

                PointStruct(

                    id=index + 1,

                    vector=embedding,

                    payload={

                        "document_id": document["id"],

                        "department": document["department"],

                        "category": document["category"],

                        "text": document["text"]

                    }

                )

            )

        self.client.upsert(

            collection_name=collection_name,

            wait=True,

            points=points

        )

        logger.info(

            f"{len(points)} points inserted."

        )

        return {

            "status": "Success",

            "collection_name": collection_name,

            "total_points": len(points),

            "message": "Points loaded successfully."

        }


    def point_count(

        self,

        collection_name: str

    ):

        logger.info(

            f"Fetching Point Count : {collection_name}"

        )

        try:

            info = self.client.get_collection(

                collection_name=collection_name

            )

        except Exception:

            return {

                "status": "Failed",

                "collection_name": collection_name,

                "total_points": 0

            }

        logger.info(

            f"Total Points : {info.points_count}"

        )

        return {

            "status": "Success",

            "collection_name": collection_name,

            "total_points": info.points_count

        }


    def delete_point(

        self,

        collection_name: str,

        point_id: int

    ):

        logger.info(

            f"Deleting Point : {point_id}"

        )

        try:

            self.client.delete(

                collection_name=collection_name,

                points_selector=[point_id]

            )

        except Exception:

            return {

                "status": "Failed",

                "message": "Point not found."

            }

        logger.info(

            "Point Deleted Successfully."

        )

        return {

            "status": "Success",

            "message": f"Point {point_id} deleted successfully."

        }
    
    # ==========================================================
    # Qdrant - Search
    # ==========================================================

    def search(

        self,

        collection_name: str,

        query: str,

        top_k: int = 3

    ):

        logger.info(

            f"Searching Collection : {collection_name}"

        )

        try:

            query_vector = EmbeddingService.generate_embedding(

                query

            )

            response = self.client.query_points(

                collection_name=collection_name,

                query=query_vector,

                limit=top_k

            )

        except Exception as ex:

            logger.error(str(ex))

            return {

                "query": query,

                "total_results": 0,

                "results": []

            }

        results = []

        for point in response.points:

            results.append(

                {

                    "point_id": str(point.id),

                    "department": point.payload.get(

                        "department"

                    ),

                    "category": point.payload.get(

                        "category"

                    ),

                    "text": point.payload.get(

                        "text"

                    ),

                    "score": round(

                        point.score,

                        4

                    )

                }

            )

        logger.info(

            "Search Completed."

        )

        return {

            "query": query,

            "total_results": len(results),

            "results": results

        }
    
    # ==========================================================
    # Qdrant - Payload Filtering
    # ==========================================================

    def payload_search(

        self,

        collection_name: str,

        query: str,

        department: str | None = None,

        category: str | None = None,

        top_k: int = 3

    ):

        logger.info(

            f"Payload Search : {collection_name}"

        )

        try:

            query_vector = EmbeddingService.generate_embedding(

                query

            )

            conditions = []

            if department:

                conditions.append(

                    FieldCondition(

                        key="department",

                        match=MatchValue(

                            value=department

                        )

                    )

                )

            if category:

                conditions.append(

                    FieldCondition(

                        key="category",

                        match=MatchValue(

                            value=category

                        )

                    )

                )

            search_filter = None

            if conditions:

                search_filter = Filter(

                    must=conditions

                )

            response = self.client.query_points(

                collection_name=collection_name,

                query=query_vector,

                filter=search_filter,

                limit=top_k

            )

        except Exception as ex:

            logger.error(str(ex))

            return {

                "query": query,

                "department": department,

                "category": category,

                "total_results": 0,

                "results": []

            }

        results = []

        for point in response.points:

            results.append(

                {

                    "point_id": str(point.id),

                    "department": point.payload["department"],

                    "category": point.payload["category"],

                    "text": point.payload["text"],

                    "score": round(

                        point.score,

                        4

                    )

                }

            )

        return {

            "query": query,

            "department": department,

            "category": category,

            "total_results": len(results),

            "results": results

        }
    

    def debug_payload(

        self,

        collection_name: str

    ):

        points, _ = self.client.scroll(

            collection_name=collection_name,

            limit=10,

            with_payload=True,

            with_vectors=False

        )

        for point in points:

            print(point.payload)

        return "Done"
    
    # ==========================================================
    # Qdrant - Keyword Search
    # ==========================================================

    def keyword_search(

        self,

        collection_name: str,

        query: str,

        top_k: int = 3

    ):

        logger.info(

            f"Keyword Search : {collection_name}"

        )

        try:

            response, _ = self.client.scroll(

                collection_name=collection_name,

                limit=100,

                with_payload=True,

                with_vectors=False

            )

        except Exception as ex:

            logger.error(str(ex))

            return []

        query = query.lower()

        results = []

        for point in response:

            text = point.payload["text"]

            score = text.lower().count(query)

            if score > 0:

                results.append(

                    {

                        "point_id": str(point.id),

                        "department": point.payload["department"],

                        "category": point.payload["category"],

                        "text": text,

                        "score": score

                    }

                )

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return results[:top_k]
    

    # ==========================================================
    # Qdrant - Hybrid Search
    # ==========================================================

    def hybrid_search(

        self,

        collection_name: str,

        query: str,

        top_k: int = 3

    ):

        logger.info(

            f"Hybrid Search : {collection_name}"

        )

        # --------------------------
        # Dense Search
        # --------------------------

        dense_results = self.search(

            collection_name,

            query,

            top_k=10

        )["results"]

        # --------------------------
        # Keyword Search
        # --------------------------

        keyword_results = self.keyword_search(

            collection_name,

            query,

            top_k=10

        )

        merged = {}

        # --------------------------
        # Dense Score
        # --------------------------

        for item in dense_results:

            merged[item["point_id"]] = item

            merged[item["point_id"]]["hybrid_score"] = item["score"]

        # --------------------------
        # Keyword Score
        # --------------------------

        for item in keyword_results:

            point_id = item["point_id"]

            if point_id in merged:

                merged[point_id]["hybrid_score"] += item["score"]

            else:

                merged[point_id] = item

                merged[point_id]["hybrid_score"] = item["score"]

        final_results = sorted(

            merged.values(),

            key=lambda x: x["hybrid_score"],

            reverse=True

        )

        return {

            "query": query,

            "total_results": min(

                top_k,

                len(final_results)

            ),

            "results": final_results[:top_k]

        }
    
    # ==========================================================
    # Qdrant - Named Vector Collection
    # ==========================================================

    def create_named_vector_collection(

        self,

        collection_name: str

    ):

        logger.info(

            f"Creating Named Vector Collection : {collection_name}"

        )

        try:

            self.client.create_collection(

                collection_name=collection_name,

                vectors_config={

                    "text": VectorParams(

                        size=1536,

                        distance=Distance.COSINE

                    ),

                    "summary": VectorParams(

                        size=1536,

                        distance=Distance.COSINE

                    )

                }

            )

            # =============================================
            # Create Payload Indexes
            # =============================================

            self.client.create_payload_index(

                collection_name=collection_name,

                field_name="department",

                field_schema=PayloadSchemaType.KEYWORD

            )

            self.client.create_payload_index(

                collection_name=collection_name,

                field_name="category",

                field_schema=PayloadSchemaType.KEYWORD

            )

        except Exception as ex:

            logger.error(str(ex))

            return {

                "status": "Failed",

                "collection_name": collection_name,

                "vector_names": [

                    "text",

                    "summary"

                ],

                "vector_size": 1536,

                "message": str(ex)

            }

        logger.info(

            "Named Vector Collection Created Successfully."

        )

        return {

            "status": "Success",

            "collection_name": collection_name,

            "vector_names": [

                "text",

                "summary"

            ],

            "vector_size": 1536,

            "message": "Named Vector Collection created successfully."

        }
    
    # ==========================================================
    # Qdrant - Named Vector Load
    # ==========================================================

    def load_named_vectors(

        self,

        collection_name: str

    ):

        logger.info(

            f"Loading Named Vectors into : {collection_name}"

        )

        points = []

        for index, document in enumerate(EMPLOYEE_DOCUMENTS):

            text_embedding = EmbeddingService.generate_embedding(

                document["text"]

            )

            summary_embedding = EmbeddingService.generate_embedding(

                document["summary"]

            )

            points.append(

                PointStruct(

                    id=index + 1,

                    vector={

                        "text": text_embedding,

                        "summary": summary_embedding

                    },

                    payload={

                        "document_id": document["id"],

                        "department": document["department"],

                        "category": document["category"],

                        "summary": document["summary"],

                        "text": document["text"]

                    }

                )

            )

        self.client.upsert(

            collection_name=collection_name,

            wait=True,

            points=points

        )

        logger.info(

            f"{len(points)} Named Vector Points Inserted."

        )

        return {

            "status": "Success",

            "collection_name": collection_name,

            "total_points": len(points),

            "message": "Named vectors loaded successfully."

        }
    
    # ==========================================================
    # Qdrant - Named Vector Search
    # ==========================================================

    def named_vector_search(

        self,

        collection_name: str,

        query: str,

        vector_name: str,

        top_k: int = 3

    ):

        logger.info(

            f"Named Vector Search ({vector_name}) : {collection_name}"

        )

        try:

            query_vector = EmbeddingService.generate_embedding(

                query

            )

            response = self.client.query_points(

                collection_name=collection_name,

                using=vector_name,

                query=query_vector,

                limit=top_k

            )

        except Exception as ex:

            logger.error(str(ex))

            return {

                "query": query,

                "vector_name": vector_name,

                "total_results": 0,

                "results": []

            }

        results = []

        for point in response.points:

            results.append(

                {

                    "point_id": str(point.id),

                    "department": point.payload["department"],

                    "category": point.payload["category"],

                    "text": point.payload["text"],

                    "score": round(

                        point.score,

                        4

                    )

                }

            )

        return {

            "query": query,

            "vector_name": vector_name,

            "total_results": len(results),

            "results": results

        }
