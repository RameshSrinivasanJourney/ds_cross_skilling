from app.services.code_chunker import (
    CodeChunker
)


python_code = """
from typing import List


class EmployeeService:

    def get_employee(
        self,
        employee_id: int
    ):

        return {
            "id": employee_id,
            "name": "Ramesh"
        }

    def create_employee(
        self,
        employee: dict
    ):

        print(
            f"Creating employee: "
            f"{employee}"
        )

        return employee


def calculate_salary(
    basic_salary: float,
    bonus: float
) -> float:

    return basic_salary + bonus
"""


chunks = CodeChunker.chunk_python(
    code=python_code,
    source="employee_service.py"
)


print(
    f"\nTotal chunks: {len(chunks)}"
)


for chunk in chunks:

    print(
        "\n========================================"
    )

    print(
        f"Chunk       : "
        f"{chunk['chunk_number']}"
    )

    print(
        f"Type        : "
        f"{chunk['chunk_type']}"
    )

    print(
        f"Name        : "
        f"{chunk['name']}"
    )

    print(
        f"Parent      : "
        f"{chunk['parent']}"
    )

    print(
        f"Source      : "
        f"{chunk['source']}"
    )

    print(
        f"Strategy    : "
        f"{chunk['chunking_strategy']}"
    )

    print("\nCode:")

    print(
        chunk["text"]
    )