from openai import OpenAI

from app.core.config import settings


import time

from app.services.ai_service import AIService

STREAM_DELAY = 0.1

class StreamingService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.GITHUB_TOKEN,
            base_url=settings.GITHUB_ENDPOINT
        )

    def stream_chat(self, messages):

        print(">>> StreamingService.stream_chat() called")

        stream = self.client.responses.create(
            model="gpt-4.1-mini",
            input=messages,
            stream=True
        )

        print(">>> Stream object created")

        for event in stream:
            print(">>> Event received:")
            print(event)

            yield str(event)

        print(">>> Stream completed")


    def stream_chat_sse(self, messages):

        answer = AIService.ask(messages)

        words = answer.split()

        partial = ""

        for word in words:

            partial += word + " "

            yield f"data: {partial}\n\n"

            time.sleep(STREAM_DELAY)

        yield "data: [DONE]\n\n"


    def stream_partial(self, messages):

        answer = AIService.ask(messages)

        words = answer.split()

        for word in words:

            yield f"data: {word}\n\n"

            time.sleep(STREAM_DELAY)

        yield "data: [DONE]\n\n"    