from typing import Optional

from pydantic import BaseModel
from pydantic.v1 import root_validator


class CallRequestSchema(BaseModel):
    to_floor: int
    from_floor: int
    elevator_id: int
    requested_by: Optional[str]



