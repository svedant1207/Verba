from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    filename: str
    content: str
    summary: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True