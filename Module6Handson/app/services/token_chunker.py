import logging

import tiktoken


logger = logging.getLogger("Module6")


class TokenChunker:

    # ==========================================================
    # Tokenizer
    # ==========================================================

    _encoding = None

    @classmethod
    def _get_encoding(cls):

        if cls._encoding is None:

            logger.info(
                "Loading tokenizer..."
            )

            cls._encoding = (
                tiktoken.get_encoding(
                    "cl100k_base"
                )
            )

            logger.info(
                "Tokenizer loaded."
            )

        return cls._encoding

    # ==========================================================
    # Count Tokens
    # ==========================================================

    @classmethod
    def count_tokens(
        cls,
        text: str
    ) -> int:

        if not text:

            return 0

        encoding = cls._get_encoding()

        tokens = encoding.encode(
            text
        )

        return len(tokens)

    # ==========================================================
    # Create Token Chunks
    # ==========================================================

    @classmethod
    def chunk_text(
        cls,
        text: str,
        chunk_size: int = 512,
        overlap: int = 50
    ) -> list[str]:

        if not text:

            return []

        # ------------------------------------------------------
        # Validate chunk size
        # ------------------------------------------------------

        if chunk_size <= 0:

            raise ValueError(
                "Chunk size must be greater than zero."
            )

        # ------------------------------------------------------
        # Validate overlap
        # ------------------------------------------------------

        if overlap < 0:

            raise ValueError(
                "Overlap cannot be negative."
            )

        if overlap >= chunk_size:

            raise ValueError(
                "Overlap must be smaller than chunk size."
            )

        # ------------------------------------------------------
        # Get tokenizer
        # ------------------------------------------------------

        encoding = cls._get_encoding()

        # ------------------------------------------------------
        # Convert text to tokens
        # ------------------------------------------------------

        tokens = encoding.encode(
            text
        )

        if not tokens:

            return []

        # ------------------------------------------------------
        # Calculate step
        #
        # Example:
        #
        # chunk_size = 256
        # overlap    = 50
        #
        # step = 256 - 50
        #      = 206
        # ------------------------------------------------------

        step = (
            chunk_size - overlap
        )

        chunks = []

        # ------------------------------------------------------
        # Create overlapping chunks
        # ------------------------------------------------------

        for start in range(
            0,
            len(tokens),
            step
        ):

            end = (
                start + chunk_size
            )

            chunk_tokens = tokens[
                start:end
            ]

            if not chunk_tokens:

                break

            chunk_text = (
                encoding.decode(
                    chunk_tokens
                )
            )

            chunks.append(
                chunk_text
            )

            # --------------------------------------------------
            # Stop when we reach the end
            # --------------------------------------------------

            if end >= len(tokens):

                break

        logger.info(
            f"Token chunking created "
            f"{len(chunks)} chunks "
            f"using chunk size "
            f"{chunk_size} and overlap "
            f"{overlap}."
        )

        return chunks

    # ==========================================================
    # Chunk Documents
    # ==========================================================

    @classmethod
    def chunk_documents(
        cls,
        documents: list[dict],
        chunk_size: int = 512,
        overlap: int = 50
    ) -> list[dict]:

        result = []

        # ------------------------------------------------------
        # Process each document/page
        # ------------------------------------------------------

        for document in documents:

            chunks = cls.chunk_text(
                text=document["text"],
                chunk_size=chunk_size,
                overlap=overlap
            )

            # --------------------------------------------------
            # Create metadata for each chunk
            # --------------------------------------------------

            for index, chunk in enumerate(
                chunks,
                start=1
            ):

                result.append(
                    {
                        "document_id":
                            document["document_id"],

                        "page_id":
                            document["page_id"],

                        "source":
                            document["source"],

                        "page":
                            document["page"],

                        "chunk_number":
                            index,

                        "chunking_strategy":
                            "token",

                        "chunk_size":
                            chunk_size,

                        "chunk_overlap":
                            overlap,

                        "token_count":
                            cls.count_tokens(
                                chunk
                            ),

                        "text":
                            chunk
                    }
)
        logger.info(
            f"Created {len(result)} "
            f"token-based document chunks."
        )

        return result