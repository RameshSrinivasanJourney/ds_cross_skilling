from app.prompts.components.persona import PERSONA
from app.prompts.components.tone import TONE
from app.prompts.components.scope import SCOPE
from app.prompts.components.limitations import LIMITATIONS
from app.prompts.components.out_of_scope import OUT_OF_SCOPE


SYSTEM_PROMPT = f"""
{PERSONA}

{TONE}

{SCOPE}

{LIMITATIONS}

{OUT_OF_SCOPE}
"""