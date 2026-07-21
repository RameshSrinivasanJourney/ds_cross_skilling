import numpy as np

from app.services.embedding_service import EmbeddingService
from app.data.employee_documents import EMPLOYEE_DOCUMENTS


class SemanticSearchService:

    def __init__(self):

        self.documents = EMPLOYEE_DOCUMENTS

        self.embeddings = [

            np.array(
                EmbeddingService.generate_embedding(doc),
                dtype=np.float32
            )

            for doc in self.documents

        ]

    @staticmethod
    def cosine_similarity(a, b):

        return np.dot(a, b) / (

            np.linalg.norm(a) *

            np.linalg.norm(b)

        )

    def search(self, query, top_k=3):

        query_embedding = np.array(

            EmbeddingService.generate_embedding(query),

            dtype=np.float32

        )

        scores = []

        for index, embedding in enumerate(self.embeddings):

            similarity = self.cosine_similarity(

                query_embedding,

                embedding

            )

            scores.append(

                (similarity, self.documents[index])

            )

        scores.sort(

            key=lambda x: x[0],

            reverse=True

        )

        return scores[:top_k]