from app.services.chroma_service import ChromaService

service = ChromaService()

results = service.search_documents(

    query="leave policy",

    top_k=3

)

print(results)