import faiss
import numpy as np

from app.services.embedding_service import EmbeddingService
from app.data.employee_documents import EMPLOYEE_DOCUMENTS


class FaissService:

    def __init__(self):

        self.index = None

        self.dimension = None

        self.documents = []


    # ==========================================================
    # FAISS - Create IndexFlatL2
    # ==========================================================

    def create_flat_l2(

        self,

        dimension: int

    ):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(

            dimension

        )

        self.documents = []

        return {

            "status": "Success",

            "index_type": "IndexFlatL2",

            "dimension": dimension,

            "message": "FAISS IndexFlatL2 created successfully."

        }


    # ==========================================================
    # FAISS - Load Documents
    # ==========================================================

    def load(

        self,

        collection_name: str

    ):

        if self.index is None:

            raise ValueError(

                "FAISS index has not been created."

            )


        vectors = []

        documents = []


        for document in EMPLOYEE_DOCUMENTS:

            embedding = EmbeddingService.generate_embedding(

                document["text"]

            )

            vectors.append(

                embedding

            )

            documents.append(

                document

            )


        vectors = np.array(

            vectors,

            dtype="float32"

        )


        self.index.add(

            vectors

        )

        self.documents.extend(

            documents

        )


        return {

            "status": "Success",

            "collection_name": collection_name,

            "total_vectors": self.index.ntotal,

            "message": "Vectors loaded successfully."

        }


    # ==========================================================
    # FAISS - Search
    # ==========================================================

    def search(

        self,

        query: str,

        top_k: int = 3

    ):

        if self.index is None:

            raise ValueError(

                "FAISS index has not been created."

            )


        if self.index.ntotal == 0:

            return {

                "query": query,

                "total_results": 0,

                "results": []

            }


        query_vector = EmbeddingService.generate_embedding(

            query

        )


        query_vector = np.array(

            [query_vector],

            dtype="float32"

        )


        distances, indices = self.index.search(

            query_vector,

            min(top_k, self.index.ntotal)

        )


        results = []


        for distance, index_id in zip(

            distances[0],

            indices[0]

        ):

            if index_id < 0:

                continue


            document = self.documents[index_id]


            results.append(

                {

                    "index": int(index_id),

                    "document_id": document["id"],

                    "department": document["department"],

                    "category": document["category"],

                    "text": document["text"],

                    "score": float(distance)

                }

            )


        return {

            "query": query,

            "total_results": len(results),

            "results": results

        }


    # ==========================================================
    # FAISS - Count
    # ==========================================================

    def count(self):

        if self.index is None:

            return 0

        return self.index.ntotal