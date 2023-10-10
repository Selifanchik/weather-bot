from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


class Base(DeclarativeBase):
    pass


class Userbot(Base):
    __tablename__ = 'userbot'
    
    user_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_name = Column(String, unique=True)