from app.services.chroma_service import ChromaService

service = ChromaService()

response = service.delete_document(

    "DOC001"

)

print(response)