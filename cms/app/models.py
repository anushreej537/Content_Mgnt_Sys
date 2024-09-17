from sqlalchemy import Column, Integer, String, Text
from database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, index=True)
    content = Column(Text)