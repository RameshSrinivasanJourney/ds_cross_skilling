def build_json_retry_prompt(
    invalid_output: str
):
    return f"""
The previous response was not valid JSON.

Return ONLY valid JSON.

Do not include:

- Markdown
- Explanations
- Comments
- Code blocks

Previous response:

{invalid_output}
"""