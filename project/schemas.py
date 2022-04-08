from typing import Generic, TypeVar

import pydantic
import pydantic.generics

T = TypeVar("T")


class GenericSchema(pydantic.generics.GenericModel, Generic[T]):
    pass


class Message(pydantic.BaseModel):
    message: str
