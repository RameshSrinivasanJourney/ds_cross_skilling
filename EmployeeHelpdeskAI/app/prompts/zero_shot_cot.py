def build_zero_shot_cot_prompt(
    user_question: str,
    max_words: int = 150
):
    return f"""
You are an Employee Helpdesk AI.

Answer the employee's question professionally.

Let's think step by step before providing the final answer.

Requirements:

- Explain your reasoning clearly.
- Give a professional final answer.
- Keep the response within {max_words} words.

Employee Question:

{user_question}
"""