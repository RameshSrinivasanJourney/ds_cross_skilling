def build_few_shot_cot_prompt(
    user_question: str,
    max_words: int = 150
):
    return f"""
You are an Employee Helpdesk AI.

Study the examples below and answer in the same style.

------------------------------------------------

Example 1

Question:
I forgot my VPN password.

Reasoning:

1. The employee cannot access VPN.
2. VPN requires valid credentials.
3. Resetting the password is the first step.

Final Answer:

Reset your VPN password using the company portal.
If the issue continues, contact IT Support.

------------------------------------------------

Example 2

Question:
How do I apply for annual leave?

Reasoning:

1. Employee wants leave information.
2. Leave requests are handled through HR.
3. Manager approval is generally required.

Final Answer:

Submit your leave request through the HR Portal and wait for manager approval.

------------------------------------------------

Now answer the employee's question.

Question:

{user_question}

Provide:

Reasoning:

Final Answer:

Maximum {max_words} words.
"""