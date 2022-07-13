from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), nullable=False)
    keyword = Column(String(50), nullable=False)
