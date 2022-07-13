from pydantic import BaseModel


class ExceptMessage(BaseModel):
    message: str


class PydanticExceptMessage(BaseModel):
    detail: list
