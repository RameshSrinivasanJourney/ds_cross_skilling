import chromadb

from app.core.config import settings
from app.utils.logger import logger

from app.data.employee_documents import EMPLOYEE_DOCUMENTS

from app.services.embedding_service import EmbeddingService


class ChromaService:

    # ==========================================================
    # Constructor
    # ==========================================================
    def __init__(self):

        logger.info(

            "Initializing ChromaDB..."

        )

        self.client = chromadb.PersistentClient(

            path=settings.CHROMA_DB_PATH

        )

        self.collection = self.client.get_or_create_collection(

            name=settings.CHROMA_COLLECTION_NAME

        )

        logger.info(

            "Collection ready."

        )

    # ==========================================================
    # Health
    # ==========================================================

    def health(self):

        return "ChromaDB initialized successfully."
    
    # ==========================================================
    # Document Management
    # ==========================================================

    def load_documents(self):

        logger.info("Loading Employee Documents...")
        
        ids=[
            document["id"]
            for document in EMPLOYEE_DOCUMENTS
        ]

        documents=[
            document["text"]
            for document in EMPLOYEE_DOCUMENTS
        ]

        metadatas=[
            {
                "department": document["department"],

                "category": document["category"]
            }

            for document in EMPLOYEE_DOCUMENTS
        ]

        self.collection.upsert(

        ids=ids,

        documents=documents,

        metadatas=metadatas

    )
        
        logger.info(

            f"{len(ids)} documents loaded successfully."

        )

        return {

            "status": "Success",

            "message": f"{len(ids)} documents loaded into ChromaDB."

        }
    
    def search_documents(
        self,
        query: str,
        top_k: int = 3
    ):

        logger.info(

            f"Searching for: {query}"

        )

        response = self.collection.query(

            query_texts=[query],

            n_results=top_k

        )

        # No documents found
        if (
            not response["ids"] or
            len(response["ids"][0]) == 0
        ):

            logger.info(

                "No matching documents found."

            )

            return {

                "query": query,

                "total_results": 0,

                "results": []

            }

        ids = response["ids"][0]

        documents = response["documents"][0]

        metadatas = response["metadatas"][0]

        distances = response["distances"][0]

        results = []

        for index in range(len(ids)):

            results.append(

                {

                    "document_id": ids[index],

                    "department": metadatas[index]["department"],

                    "category": metadatas[index]["category"],

                    "text": documents[index],

                    "distance": round(

                        distances[index],

                        4

                    )

                }

            )

        logger.info(

            f"{len(results)} documents found."

        )

        return {

            "query": query,

            "total_results": len(results),

            "results": results

        }
    
    def delete_document(
            self,
            document_id:str
    ):
        logger.info(f"deleting Document: {document_id}")

        self.collection.delete(
            ids=[document_id]
        )

        logger.info(

            "Document deleted successfully."

        )

        return {

            "status": "Success",

            "message": f"{document_id} deleted successfully."

        }
    
    def delete_documents(

        self,

        document_ids: list[str]

    ):

        logger.info(

            f"Deleting {len(document_ids)} documents."

        )

        self.collection.delete(

            ids=document_ids

        )

        logger.info(

            "Documents deleted successfully."

        )

        return {

            "status": "Success",

            "message": f"{len(document_ids)} documents deleted successfully."

        }
    
    def delete_all_documents(self):

        logger.info(

            "Deleting all documents..."

        )

        self.client.delete_collection(

            settings.CHROMA_COLLECTION_NAME

        )

        self.collection = self.client.get_or_create_collection(

            settings.CHROMA_COLLECTION_NAME

        )

        logger.info(

            "All documents deleted successfully."

        )

        return {

            "status": "Success",

            "message": "All documents deleted successfully."

        }

    # ==========================================================
    # Collection Management
    # ==========================================================

    def list_collections(self):

        logger.info(

            "Fetching all collections..."

        )

        collections = self.client.list_collections()

        collection_names = [

            collection.name

            for collection in collections

        ]

        logger.info(

            f"{len(collection_names)} collections found."

        )

        return {

            "status": "Success",

            "total_collections": len(collection_names),

            "collections": collection_names

        }
    
    def collection_info(
        self,
        collection_name: str
    ):

        logger.info(

            f"Fetching information for collection: {collection_name}"

        )

        collection = self.client.get_collection(

            name=collection_name

        )

        document_count = collection.count()

        logger.info(

            "Collection information fetched successfully."

        )

        return {

            "status": "Success",

            "collection_name": collection.name,

            "document_count": document_count

        }
    
    def document_count(self):

        logger.info(

            "Fetching document count..."

        )

        count = self.collection.count()

        logger.info(

            f"Total Documents : {count}"

        )

        return {

            "status": "Success",

            "total_documents": count

        }
    
    def peek_documents(
        self,
        limit: int
    ):

        logger.info(

            f"Fetching first {limit} documents..."

        )

        response = self.collection.peek(

            limit=limit

        )

        ids = response["ids"]
        documents = response["documents"]
        metadatas = response["metadatas"]

        results = []

        for index in range(len(ids)):

            results.append(

                {

                    "document_id": ids[index],

                    "department": metadatas[index]["department"],

                    "category": metadatas[index]["category"],

                    "text": documents[index]

                }

            )

        logger.info(

            f"{len(results)} documents returned."

        )

        return {

            "status": "Success",

            "total_documents": len(results),

            "documents": results

        }
    
    # ==========================================================
    # Embedding Management
    # ==========================================================

    def load_embedded_documents(self):

        logger.info(

            "Loading Employee Documents with Explicit Embeddings..."

        )

        ids = [
            document["id"]
            for document in EMPLOYEE_DOCUMENTS
        ]

        documents = [
            document["text"]
            for document in EMPLOYEE_DOCUMENTS
        ]

        embeddings = [
            EmbeddingService.generate_embedding(document)
            for document in documents
        ]

        metadatas = [
            {
                "department": document["department"],
                "category": document["category"]
            }
            for document in EMPLOYEE_DOCUMENTS
        ]

        self.collection.upsert(

            ids=ids,

            documents=documents,

            embeddings=embeddings,

            metadatas=metadatas

        )

        logger.info(

            f"{len(ids)} embedded documents loaded successfully."

        )

        return {

            "status": "Success",

            "message": f"{len(ids)} embedded documents loaded successfully."

        }
    
    def vector_search(

        self,

        query: str,

        top_k: int = 3

    ):

        logger.info(

            f"Vector Searching: {query}"

        )

        query_embedding = EmbeddingService.generate_embedding(

            query

        )

        response = self.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k

        )

        results = []

        ids = response["ids"][0]
        documents = response["documents"][0]
        metadatas = response["metadatas"][0]
        distances = response["distances"][0]

        for index in range(len(ids)):

            results.append(

                {

                    "document_id": ids[index],

                    "department": metadatas[index]["department"],

                    "category": metadatas[index]["category"],

                    "text": documents[index],

                    "distance": round(

                        distances[index],

                        4

                    )

                }

            )

        logger.info(

            "Vector Search Completed."

        )

        return {

            "query": query,

            "total_results": len(results),

            "results": results

        }
    
    # ==========================================================
    # Metadata Filtering
    # ==========================================================

    def metadata_search(

        self,

        query: str,

        department: str | None = None,

        category: str | None = None,

        top_k: int = 3

    ):

        logger.info(

            f"Metadata Search : {query}"

        )

        filters = []

        if department:

            filters.append(

                {

                    "department": department

                }

            )

        if category:

            filters.append(

                {

                    "category": category

                }

            )

        if len(filters) == 0:

            where_filter = None

        elif len(filters) == 1:

            where_filter = filters[0]

        else:

            where_filter = {

                "$and": filters

            }

        logger.info(

            f"Where Filter : {where_filter}"

        )

        if where_filter:

            response = self.collection.query(

                query_texts=[query],

                where=where_filter,

                n_results=top_k

            )

        else:

            response = self.collection.query(

                query_texts=[query],

                n_results=top_k

            )

        results = []

        ids = response["ids"][0]
        documents = response["documents"][0]
        metadatas = response["metadatas"][0]
        distances = response["distances"][0]

        for index in range(len(ids)):

            results.append(

                {

                    "document_id": ids[index],

                    "department": metadatas[index]["department"],

                    "category": metadatas[index]["category"],

                    "text": documents[index],

                    "distance": round(

                        distances[index],

                        4

                    )

                }

            )

        logger.info(

            "Metadata Search Completed."

        )

        return {

            "query": query,

            "department": department,

            "category": category,

            "total_results": len(results),

            "results": results

        }
    
    # ==========================================================
    # Storage
    # ==========================================================
    def memory_demo(self):

        logger.info(

            "Initializing In-Memory ChromaDB..."

        )

        memory_client = chromadb.Client()

        collection = memory_client.get_or_create_collection(

            name="memory_demo"

        )

        ids = [
            document["id"]
            for document in EMPLOYEE_DOCUMENTS
        ]

        documents = [
            document["text"]
            for document in EMPLOYEE_DOCUMENTS
        ]

        metadatas = [
            {
                "department": document["department"],
                "category": document["category"]
            }
            for document in EMPLOYEE_DOCUMENTS
        ]

        collection.upsert(

            ids=ids,

            documents=documents,

            metadatas=metadatas

        )

        count = collection.count()

        logger.info(

            "In-Memory Collection Created Successfully."

        )

        return {

            "status": "Success",

            "storage_type": "In-Memory",

            "collection_name": "memory_demo",

            "total_documents": count,

            "message": "Documents stored in memory successfully."

        }




