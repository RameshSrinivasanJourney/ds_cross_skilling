import faiss
import numpy as np

from app.services.embedding_service import EmbeddingService
from app.data.employee_documents import EMPLOYEE_DOCUMENTS


class FAISSService:

    def __init__(self):

        self.documents = EMPLOYEE_DOCUMENTS

        embeddings = [

            EmbeddingService.generate_embedding(doc)

            for doc in self.documents

        ]

        self.embeddings = np.array(

            embeddings,

            dtype=np.float32

        )

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        faiss.normalize_L2(self.embeddings)

        self.index.add(self.embeddings)

    def search(self, query, top_k=3):

        query_embedding = np.array(

            [EmbeddingService.generate_embedding(query)],

            dtype=np.float32

        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(

            query_embedding,

            top_k

        )

        results = []

        for score, idx in zip(

            scores[0],

            indices[0]

        ):

            results.append(

                {

                    "similarity": float(score),

                    "document": self.documents[idx]

                }

            )

        return results