from sqlalchemy import Integer, Column, String

from app.models.base import Base


class Reply(Base):
    __tablename__ = "replies"

    id = Column(Integer, primary_key=True)
    feed_id = Column(Integer, nullable=False)
    parent_id = Column(Integer)
    depth = Column(Integer, default=0)
    nickname = Column(String(50), nullable=False)
    comment = Column(String(255), nullable=False)
