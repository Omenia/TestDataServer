import os.path

from config import db


def setup():
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testitem.db'))
    if not os.path.exists(db_file):
        create()


def create():
    db.create_all()
    db.session.commit()
