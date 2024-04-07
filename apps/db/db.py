import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from apps.constants_access import DIALECT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, HOST
from apps.db.db_structure import UserBot
from apps.db.db_structure import Base


engine = create_engine(f"{DIALECT}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}/{POSTGRES_DB}")


def add_user(first_name, user_chatid, user_name):
    Base.metadata.create_all(engine)
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(UserBot).filter_by(user_chatid=user_chatid).first()
        if not query:
            title = UserBot(first_name=first_name, user_chatid=user_chatid, user_name=user_name)
            db.add(title)
        else:
            query.first_name = first_name
            query.username = user_name
        db.commit()


def get_user(id):
    with Session(autoflush=False, bind=engine) as db:
        a = db.query(UserBot).filter_by(user_chatid=id).first()
    return a.first_name


