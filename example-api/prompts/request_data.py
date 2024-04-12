from pydantic import BaseModel


class PromptBody(BaseModel):
    prompt: str


class ImagePromptBody(PromptBody):
    number_of_images: int