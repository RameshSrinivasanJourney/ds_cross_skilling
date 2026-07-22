from app.services.chroma_service import ChromaService

service = ChromaService()

response = service.load_documents()

print(response)