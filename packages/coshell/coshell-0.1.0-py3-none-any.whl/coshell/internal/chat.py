from typing import List

from coshell.internal.openai.api import Api
from coshell.internal.openai.chat_completions import ChatCompletionsMessage, ChatCompletions, ChatCompletionsRequestPayload


class Chat:

    def __init__(self):
        self.chat_completions: ChatCompletions = ChatCompletions(Api())
        self.messages: List[ChatCompletionsMessage] = []

    def get_payload(self) -> ChatCompletionsRequestPayload:
        return ChatCompletionsRequestPayload(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.3,
        )

    def add_message(self, content: str):
        message = ChatCompletionsMessage(role="user", content=content)
        self.messages.append(message)

    def send_message(self, content: str) -> str:
        message = ChatCompletionsMessage(role="user", content=content)
        self.messages.append(message)
        response_payload = self.chat_completions.post(self.get_payload())
        response_message = response_payload.choices[0].message
        self.messages.append(response_message)
        return response_message.content
