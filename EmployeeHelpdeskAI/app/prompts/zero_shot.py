def build_zero_shot_prompt(
    user_question: str,
    max_words: int = 150
):
    return f"""
<instructions>

Answer professionally.
Use simple English.
Maximum {max_words} words.

</instructions>

<employee_question>

{user_question}

</employee_question>
"""