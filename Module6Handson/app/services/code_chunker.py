import ast
import logging

logger = logging.getLogger("Module6")


class CodeChunker:

    # ==========================================================
    # Parse Python Code
    # ==========================================================

    @staticmethod
    def parse_python_code(
        code: str
    ):

        try:

            return ast.parse(code)

        except SyntaxError as exc:

            logger.error(
                f"Unable to parse Python code: {exc}"
            )

            raise ValueError(
                "Invalid Python code."
            ) from exc

    # ==========================================================
    # Extract Functions
    # ==========================================================

    @staticmethod
    def extract_function_source(
        code_lines: list[str],
        node
    ) -> str:

        start_line = node.lineno - 1

        end_line = node.end_lineno

        return "\n".join(
            code_lines[
                start_line:end_line
            ]
        )

    # ==========================================================
    # Chunk Python Code
    # ==========================================================

    @classmethod
    def chunk_python(
        cls,
        code: str,
        source: str = "unknown.py"
    ) -> list[dict]:

        if not code.strip():

            return []

        tree = cls.parse_python_code(
            code
        )

        code_lines = code.splitlines()

        chunks = []

        # ======================================================
        # Walk Top-Level Nodes
        # ======================================================

        for node in tree.body:

            # --------------------------------------------------
            # Class
            # --------------------------------------------------

            if isinstance(
                node,
                ast.ClassDef
            ):

                class_source = (
                    cls.extract_function_source(
                        code_lines,
                        node
                    )
                )

                chunks.append(
                    {
                        "source": source,
                        "chunk_type": "class",
                        "name": node.name,
                        "parent": None,
                        "text": class_source
                    }
                )

                # --------------------------------------------------
                # Extract methods separately
                # --------------------------------------------------

                for child in node.body:

                    if isinstance(
                        child,
                        (
                            ast.FunctionDef,
                            ast.AsyncFunctionDef
                        )
                    ):

                        method_source = (
                            cls.extract_function_source(
                                code_lines,
                                child
                            )
                        )

                        chunks.append(
                            {
                                "source": source,
                                "chunk_type": "method",
                                "name": child.name,
                                "parent": node.name,
                                "text": method_source
                            }
                        )

            # --------------------------------------------------
            # Top-level function
            # --------------------------------------------------

            elif isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef
                )
            ):

                function_source = (
                    cls.extract_function_source(
                        code_lines,
                        node
                    )
                )

                chunks.append(
                    {
                        "source": source,
                        "chunk_type": "function",
                        "name": node.name,
                        "parent": None,
                        "text": function_source
                    }
                )

            # --------------------------------------------------
            # Imports
            # --------------------------------------------------

            elif isinstance(
                node,
                (
                    ast.Import,
                    ast.ImportFrom
                )
            ):

                import_source = (
                    cls.extract_function_source(
                        code_lines,
                        node
                    )
                )

                chunks.append(
                    {
                        "source": source,
                        "chunk_type": "import",
                        "name": None,
                        "parent": None,
                        "text": import_source
                    }
                )

        # ======================================================
        # Add Metadata
        # ======================================================

        for index, chunk in enumerate(
            chunks,
            start=1
        ):

            chunk["chunk_number"] = index

            chunk["chunking_strategy"] = (
                "code-aware"
            )

        logger.info(
            f"Code-aware chunking created "
            f"{len(chunks)} chunks."
        )

        return chunks