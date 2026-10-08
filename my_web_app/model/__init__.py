from pydantic import BaseModel, Field


class Example (BaseModel):
    name: str = Field()

class ExampleResponse(BaseModel):
    response: str = Field()