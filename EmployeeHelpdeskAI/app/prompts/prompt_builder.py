from app.prompts.zero_shot import build_zero_shot_prompt
from app.prompts.one_shot import build_one_shot_prompt
from app.prompts.few_shot import build_few_shot_prompt
from app.prompts.markdown_prompt import build_markdown_prompt
from app.prompts.json_prompt import build_json_prompt
from app.prompts.xml_prompt import build_xml_prompt
from app.prompts.cot_prompt import build_cot_prompt
from app.prompts.zero_shot_cot import build_zero_shot_cot_prompt
from app.prompts.few_shot_cot import build_few_shot_cot_prompt
from app.prompts.tree_of_thought import build_tree_of_thought_prompt
from app.prompts.react_prompt import build_react_prompt
from app.prompts.meta_prompt import build_meta_prompt
from app.prompts.consistent_few_shot import build_consistent_prompt
from app.prompts.runtime_context import build_runtime_context

def build_prompt(
    user_question: str,
    max_words: int = 150
):
    
    context = build_runtime_context()

    prompt = build_few_shot_prompt(
        user_question,
        max_words
    )

    return f"""
{context}

{prompt}
"""


    '''return build_consistent_prompt(
        user_question
    )'''