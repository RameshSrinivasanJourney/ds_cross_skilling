import logging
import re

logger = logging.getLogger("Module6")


class MarkdownChunker:

    # ==========================================================
    # Chunk Markdown Text
    # ==========================================================

    @classmethod
    def chunk_text(
        cls,
        text: str,
        max_chunk_size: int = 1000
    ) -> list[dict]:

        if not text:
            return []

        lines = text.splitlines()

        chunks = []

        current_heading = None
        current_level = None
        current_content = []

        def flush_chunk():

            if not current_content:
                return

            content = "\n".join(
                current_content
            ).strip()

            if not content:
                return

            # --------------------------------------------------
            # Split oversized sections
            # --------------------------------------------------

            if len(content) <= max_chunk_size:

                chunks.append(
                    {
                        "heading": current_heading,
                        "heading_level": current_level,
                        "text": content
                    }
                )

                return

            # --------------------------------------------------
            # Simple paragraph-based split
            # --------------------------------------------------

            paragraphs = re.split(
                r"\n\s*\n",
                content
            )

            temp = []

            temp_length = 0

            for paragraph in paragraphs:

                paragraph = paragraph.strip()

                if not paragraph:
                    continue

                additional_length = (
                    len(paragraph) + 2
                )

                if (
                    temp
                    and
                    temp_length
                    + additional_length
                    > max_chunk_size
                ):

                    chunks.append(
                        {
                            "heading":
                                current_heading,

                            "heading_level":
                                current_level,

                            "text":
                                "\n\n".join(temp)
                        }
                    )

                    temp = []
                    temp_length = 0

                temp.append(paragraph)

                temp_length += additional_length

            if temp:

                chunks.append(
                    {
                        "heading":
                            current_heading,

                        "heading_level":
                            current_level,

                        "text":
                            "\n\n".join(temp)
                    }
                )

        # ======================================================
        # Process Markdown Lines
        # ======================================================

        for line in lines:

            heading_match = re.match(
                r"^(#{1,6})\s+(.+?)\s*$",
                line
            )

            if heading_match:

                flush_chunk()

                current_content = []

                current_level = len(
                    heading_match.group(1)
                )

                current_heading = (
                    heading_match.group(2)
                )

                continue

            current_content.append(
                line
            )

        # ======================================================
        # Final Chunk
        # ======================================================

        flush_chunk()

        # ======================================================
        # Add Chunk Numbers
        # ======================================================

        for index, chunk in enumerate(
            chunks,
            start=1
        ):

            chunk["chunk_number"] = index

            chunk["chunking_strategy"] = (
                "markdown"
            )

        logger.info(
            f"Markdown chunking created "
            f"{len(chunks)} chunks."
        )

        return chunks

    # ==========================================================
    # Chunk Documents
    # ==========================================================

    @classmethod
    def chunk_documents(
        cls,
        documents: list[dict],
        max_chunk_size: int = 1000
    ) -> list[dict]:

        result = []

        for document in documents:

            markdown_chunks = cls.chunk_text(
                text=document["text"],
                max_chunk_size=max_chunk_size
            )

            for chunk in markdown_chunks:

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

                        "heading":
                            chunk["heading"],

                        "heading_level":
                            chunk["heading_level"],

                        "chunk_number":
                            chunk["chunk_number"],

                        "chunking_strategy":
                            chunk["chunking_strategy"],

                        "text":
                            chunk["text"]
                    }
                )

        logger.info(
            f"Created {len(result)} "
            f"Markdown document chunks."
        )

        return result