import logging

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


logger = logging.getLogger("Module6")


class RecursiveChunker:

    # ==========================================================
    # Create Recursive Text Splitter
    # ==========================================================

    @staticmethod
    def create_splitter(
        chunk_size: int = 1000,
        chunk_overlap: int = 100
    ):

        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than zero."
            )

        if chunk_overlap < 0:
            raise ValueError(
                "chunk_overlap cannot be negative."
            )

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller "
                "than chunk_size."
            )

        return RecursiveCharacterTextSplitter(

            chunk_size=chunk_size,

            chunk_overlap=chunk_overlap,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],

            length_function=len,

            is_separator_regex=False
        )

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

        splitter = cls.create_splitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        chunks = []

        for document in documents:

            text_chunks = splitter.split_text(
                document["text"]
            )

            for chunk_number, chunk_text in enumerate(
                text_chunks,
                start=1
            ):

                chunk_id = (
                    f"{document['page_id']}"
                    f"_rc_c{chunk_number}"
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

                        "chunking_strategy":
                            "recursive_character",

                        "text":
                            chunk_text
                    }
                )

        logger.info(
            f"Recursive chunking created "
            f"{len(chunks)} chunks."
        )

        return chunks