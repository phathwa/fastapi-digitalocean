from pydantic import BaseModel

class ItemCreate(BaseModel):
    id: int
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
