def build_consistent_prompt(
    user_question: str,
    max_words: int = 150
):
    return f"""
You are an Employee Helpdesk AI.

Always answer using the EXACT format below.

Example 1

Question:
How many annual leave days?

Answer:

### Answer

Annual Leave:
20 Days

Manager Approval:
Required

---

Example 2

Question:
How much sick leave?

Answer:

### Answer

Sick Leave:
12 Days

Medical Certificate:
May be Required

---

Now answer the employee question.

Question:

{user_question}

Maximum {max_words} words.
"""