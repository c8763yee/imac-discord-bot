from typing import Any
from pydantic import BaseModel

class Field(BaseModel):
    """
    data class of Field inside Embed message
    """
    name: str
    value: Any
    inline: bool = False
