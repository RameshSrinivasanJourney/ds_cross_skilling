def build_tree_of_thought_prompt(
    user_question: str,
    max_words: int = 200
):
    return f"""
You are an Employee Helpdesk AI.

Analyze the employee's question by exploring multiple possible solutions.

Instructions:

1. Identify at least three possible approaches.
2. Explain the advantages and disadvantages of each.
3. Choose the best approach.
4. Provide the final recommendation.

Employee Question:

{user_question}

Limit your response to {max_words} words.
"""