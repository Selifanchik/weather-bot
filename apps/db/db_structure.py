from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


class Base(DeclarativeBase):
    pass


class UserBot(Base):
    __tablename__ = 'user_bot'
    
    user_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    first_name = Column(String)
    user_chatid = Column(String, unique=True)
    user_name = Column(String)
