from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from apps.constants_access import DIALECT, DATABASE, LOGIN, PASSWORD, HOST
from apps.db_structure import Userbot
from apps.db_structure import Base


engine = create_engine(f"{DIALECT}://{LOGIN}:{PASSWORD}@{HOST}/{DATABASE}")


def add_user(first_name, user_chatid, username):
    Base.metadata.create_all(engine)
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Userbot).filter_by(user_chatid=user_chatid).first()
        if not query:
            title = Userbot(first_name=first_name, user_chatid=user_chatid, username=username)
            db.add(title)
        else:
            query.first_name = first_name
            query.username = username
        db.commit()


def get_user(id):
    with Session(autoflush=False, bind=engine) as db:
        a = db.query(Userbot).filter_by(user_chatid=id).first()
    return a.first_name


