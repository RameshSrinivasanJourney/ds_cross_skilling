import logging
import os

from app.services.pdf_loader import PDFLoader


logger = logging.getLogger("Module6")


class IngestionService:

    # ==========================================================
    # Ingest Document
    # ==========================================================

    @classmethod
    def ingest(
        cls,
        file_path: str
    ) -> list[dict]:

        logger.info(
            f"Ingesting document: {file_path}"
        )

        # ------------------------------------------------------
        # Validate file
        # ------------------------------------------------------

        if not os.path.exists(file_path):

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        # ------------------------------------------------------
        # Determine file type
        # ------------------------------------------------------

        extension = (
            os.path.splitext(
                file_path
            )[1]
            .lower()
        )

        # ------------------------------------------------------
        # PDF
        # ------------------------------------------------------

        if extension == ".pdf":

            documents = PDFLoader.load(
                file_path
            )

        else:

            raise ValueError(
                f"Unsupported file type: "
                f"{extension}"
            )

        logger.info(
            f"Ingestion completed. "
            f"Loaded {len(documents)} "
            f"document sections."
        )

        return documents