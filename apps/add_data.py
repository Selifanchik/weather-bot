from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from apps.constants_access import DIALECT, DATABASE, LOGIN, PASSWORD, HOST
from apps.db_structure import Userbot
from apps.db_structure import Base


engine = create_engine(f"{DIALECT}://{LOGIN}:{PASSWORD}@{HOST}/{DATABASE}")


def add_data():
     Base.metadata.create_all(engine)
     with Session(autoflush=False, bind=engine) as db:
         title = Userbot(user_name='Selifanchik')
         db.add(title)
         db.commit()


def get_user():
    with Session(autoflush=False, bind=engine) as db:
        a = db.query(Userbot).first()
    return a.user_name


