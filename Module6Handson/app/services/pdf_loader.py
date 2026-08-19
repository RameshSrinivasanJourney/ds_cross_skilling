import logging
import re
from pathlib import Path

import fitz


logger = logging.getLogger("Module6")


class PDFLoader:

    # ==========================================================
    # Generate Document ID
    # ==========================================================

    @staticmethod
    def _generate_document_id(
        file_name: str
    ) -> str:

        document_id = Path(
            file_name
        ).stem.lower()

        document_id = re.sub(
            r"[^a-z0-9]+",
            "_",
            document_id
        )

        return document_id.strip("_")

    # ==========================================================
    # Load PDF
    # ==========================================================

    @classmethod
    def load(
        cls,
        file_path: str
    ) -> list[dict]:

        path = Path(file_path)

        if not path.exists():

            raise FileNotFoundError(
                f"PDF file not found: {file_path}"
            )

        if path.suffix.lower() != ".pdf":

            raise ValueError(
                "File must be a PDF."
            )

        document_id = (
            cls._generate_document_id(
                path.name
            )
        )

        logger.info(
            f"Loading PDF : {path.name}"
        )

        documents = []

        pdf = fitz.open(file_path)

        try:

            for page_number, page in enumerate(
                pdf,
                start=1
            ):

                text = page.get_text(
                    "text"
                ).strip()

                if not text:

                    logger.warning(
                        f"No text found on page "
                        f"{page_number}"
                    )

                    continue

                page_id = (
                    f"{document_id}_p{page_number}"
                )

                documents.append(
                    {
                        "document_id": document_id,
                        "page_id": page_id,
                        "source": path.name,
                        "page": page_number,
                        "text": text
                    }
                )

        finally:

            pdf.close()

        logger.info(
            f"PDF loaded successfully. "
            f"Pages extracted: {len(documents)}"
        )

        return documents

    # ==========================================================
    # Chunk Documents
    # ==========================================================

    @classmethod
    def chunk_documents(
        cls,
        documents: list[dict],
        chunk_size: int = 1000,
        chunk_overlap: int = 100
    ) -> list[dict]:

        chunks = []

        for document in documents:

            text_chunks = cls.chunk_text(
                text=document["text"],
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

            for chunk_number, chunk_text in enumerate(
                text_chunks,
                start=1
            ):

                chunk_id = (
                    f"{document['page_id']}"
                    f"_c{chunk_number}"
                )

                chunks.append(
                    {
                        "document_id":
                            document["document_id"],

                        "page_id":
                            document["page_id"],

                        "chunk_id":
                            chunk_id,

                        "source":
                            document["source"],

                        "page":
                            document["page"],

                        "chunk_number":
                            chunk_number,

                        "text":
                            chunk_text
                    }
                )

        logger.info(
            f"Created {len(chunks)} "
            f"document chunks."
        )

        return chunks