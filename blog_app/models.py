from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String, index=True, default="Journal")
    summary = Column(String, nullable=True)
    content = Column(Text)
    featured_image = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
