class PromptVersionService:

    @staticmethod
    def get_prompt_version(version: str):

        if version == "v1":

            from app.prompts.versions.hr_prompt_v1 import HR_PROMPT_V1

            return HR_PROMPT_V1
    
        if version == "v2":

            from app.prompts.versions.hr_prompt_v2 import HR_PROMPT_V2

            return HR_PROMPT_V2

        return None