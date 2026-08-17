# ==========================================================
# FAISS - Sentence Transformer
# ==========================================================

import logging

import faiss
import numpy as np

from app.core.config import settings
from app.services.embedding_service import EmbeddingService
from app.data.employee_documents import EMPLOYEE_DOCUMENTS


logger = logging.getLogger("Module5")


class FAISSSTService:

    index = None

    documents = []

    # ======================================================
    # Create IndexFlatL2
    # ======================================================

    @classmethod
    def create_flat_l2(cls):

        logger.info(
            "Creating FAISS Sentence Transformer IndexFlatL2..."
        )

        cls.index = faiss.IndexFlatL2(
            settings.FAISS_ST_DIMENSION
        )

        cls.documents = []

        logger.info(
            "FAISS Sentence Transformer IndexFlatL2 created."
        )

        return {
            "status": "Success",
            "dimension": settings.FAISS_ST_DIMENSION,
            "index_type": "IndexFlatL2",
            "message": (
                "FAISS Sentence Transformer "
                "IndexFlatL2 created successfully."
            )
        }

    # ==========================================================
    # Load Documents
    # ==========================================================

    @classmethod
    def load_documents(

        cls,

        collection_name: str

    ):

        logger.info(

            f"Loading Documents into FAISS : {collection_name}"

        )

        if cls.index is None:

            cls.create_flat_l2()

        # ------------------------------------------------------
        # Load documents from existing project data
        # ------------------------------------------------------

        if collection_name == "employee_documents":

            documents = EMPLOYEE_DOCUMENTS

        else:

            return {

                "status": "Failed",

                "total_documents": 0,

                "dimension": settings.FAISS_ST_DIMENSION,

                "message": (
                    f"Unknown collection: {collection_name}"
                )

            }

        # ------------------------------------------------------
        # Generate embeddings
        # ------------------------------------------------------

        vectors = []

        for document in documents:

            embedding = (
                EmbeddingService.generate_embedding(
                    document["text"]
                )
            )

            vectors.append(embedding)

        vectors = np.array(

            vectors,

            dtype="float32"

        )

        # ------------------------------------------------------
        # Add vectors to FAISS
        # ------------------------------------------------------

        cls.index.add(vectors)

        cls.documents.extend(documents)

        logger.info(

            f"{len(documents)} vectors loaded into FAISS."

        )

        return {

            "status": "Success",

            "total_documents": len(
                cls.documents
            ),

            "dimension": settings.FAISS_ST_DIMENSION,

            "message": (
                "Documents loaded successfully."
            )

        }

    # ======================================================
    # Search
    # ======================================================

    @classmethod
    def search(
        cls,
        query: str,
        top_k: int = 3
    ):

        if cls.index is None:

            return {
                "query": query,
                "total_results": 0,
                "results": []
            }

        if cls.index.ntotal == 0:

            return {
                "query": query,
                "total_results": 0,
                "results": []
            }

        query_embedding = (
            EmbeddingService.generate_embedding(
                query
            )
        )

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = cls.index.search(
            query_vector,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:
                continue

            document = cls.documents[index]

            results.append(
                {
                    "point_id": str(
                        document["id"]
                    ),
                    "department": document[
                        "department"
                    ],
                    "category": document[
                        "category"
                    ],
                    "text": document[
                        "text"
                    ],
                    "distance": round(
                        float(distance),
                        4
                    )
                }
            )

        return {
            "query": query,
            "total_results": len(results),
            "results": results
        }

    # ======================================================
    # Count
    # ======================================================

    @classmethod
    def count(cls):

        if cls.index is None:

            return {
                "status": "Success",
                "total_vectors": 0
            }

        return {
            "status": "Success",
            "total_vectors": cls.index.ntotal
        }