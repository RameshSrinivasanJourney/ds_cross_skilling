from app.services.semantic_search_service import SemanticSearchService


class HybridSearchService:

    def __init__(self):

        self.semantic = SemanticSearchService()

    def keyword_score(self, query: str, document: str):

        query_words = query.lower().split()
        document = document.lower()

        matches = sum(
            1
            for word in query_words
            if word in document
        )

        return matches / max(len(query_words), 1)

    def search(self, query: str):

        semantic_results = self.semantic.search(
            query,
            top_k=len(self.semantic.documents)
        )

        results = []

        for semantic_score, document in semantic_results:

            keyword = self.keyword_score(
                query,
                document
            )

            final_score = (

                0.4 * keyword +

                0.6 * semantic_score

            )

            results.append({

                "document": document,

                "keyword_score": round(keyword, 3),

                "semantic_score": round(float(semantic_score), 3),

                "final_score": round(float(final_score), 3)

            })

        results.sort(

            key=lambda x: x["final_score"],

            reverse=True

        )

        return results