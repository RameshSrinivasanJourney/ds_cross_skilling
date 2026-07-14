def build_meta_prompt(
    user_question: str,
    max_words: int = 200
):
    return f"""
You are a Prompt Engineering expert.

Your task is to improve the user's prompt before answering it.

Follow these steps:

1. Rewrite the user's prompt to make it clearer.
2. Explain why the rewritten prompt is better.
3. Answer the rewritten prompt.
4. Keep the final response within {max_words} words.

Original Prompt:

{user_question}
"""