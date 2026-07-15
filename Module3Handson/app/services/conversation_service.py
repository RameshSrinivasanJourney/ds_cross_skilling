conversation_history = [
    {
        "role":"system",
        "content":"You are a helpful HR Assistant."
    }
]

class ConversationService :
    @staticmethod
    def add_user_message(message:str):
        conversation_history.append(
            {
                 "role": "user",
                "content": message
            }
        )

    @staticmethod
    def add_assistant_message(message:str):
        conversation_history.append(
            {
                 "role": "assistant",
                "content": message
            }
        )


    @staticmethod
    def get_messages():
        return conversation_history
