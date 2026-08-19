from app.services.pdf_loader import PDFLoader


pdf_path = (
    "documents/Leave Policy.pdf"
)


documents = PDFLoader.load(
    pdf_path
)


print(
    f"\nTotal pages extracted: "
    f"{len(documents)}"
)


for document in documents:

    print("\n===================================")

    print(
        f"Document ID : "
        f"{document['document_id']}"
    )

    print(
        f"Page ID     : "
        f"{document['page_id']}"
    )

    print(
        f"Source      : "
        f"{document['source']}"
    )

    print(
        f"Page        : "
        f"{document['page']}"
    )

    print("\nText:")

    print(
        document["text"][:1000]
    )