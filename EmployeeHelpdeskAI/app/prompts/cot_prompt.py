def build_cot_prompt(
    question: str,
    max_words: int = 150
):
    return f"""
Answer the following employee question.

Question:
{question}

Explain your reasoning step by step.

Finally provide the final answer.

Maximum {max_words} words.
"""