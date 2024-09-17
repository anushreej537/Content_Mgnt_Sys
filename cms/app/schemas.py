from pydantic import BaseModel

class PostBase(BaseModel):
    title : str
    content : str


class PostCreate(BaseModel):
    title :str
    content : str


class Post(PostBase):
    id : int

    class Config:
        orm_mode = True