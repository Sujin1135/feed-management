from sqlalchemy import Column, Integer, String, Text

from app.models.base import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), nullable=False)
    password = Column(String(60), nullable=False)
    title = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)
