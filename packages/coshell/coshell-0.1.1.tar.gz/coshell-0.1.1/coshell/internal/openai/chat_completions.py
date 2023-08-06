from typing import List, Optional

from pydantic import BaseModel

from coshell.internal.openai.api import Api
from coshell.internal.openai.endpoint import Endpoint


class ChatCompletionsMessage(BaseModel):
    role: str
    content: str


class ChatCompletionsRequestPayload(BaseModel):
    model: str
    messages: List[ChatCompletionsMessage]
    temperature: Optional[float]


class ChatCompletionsResponseChoice(BaseModel):
    index: int
    message: ChatCompletionsMessage
    finish_reason: str


class ChatCompletionsResponseUsage(BaseModel):
    prompt_tokens: str
    completion_tokens: str
    total_tokens: str


class ChatCompletionsResponsePayload(BaseModel):
    id: str
    object: str
    created: str
    choices: List[ChatCompletionsResponseChoice]
    usage: ChatCompletionsResponseUsage


class ChatCompletions:

    def __init__(self, api: Api):
        self.endpoint: Endpoint = Endpoint(api, "chat/completions")

    def post(self, payload: ChatCompletionsRequestPayload) -> ChatCompletionsResponsePayload:
        return ChatCompletionsResponsePayload.parse_obj(self.endpoint.post(payload.dict()))
