from app.services.embedding_service import EmbeddingService

embedding = EmbeddingService.generate_embedding(

    "Employees may work remotely."

)

print(len(embedding))
print(embedding[:5])