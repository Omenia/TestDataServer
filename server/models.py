from datetime import datetime

from config import db, ma


class TestItem(db.Model):

    __tablename__ = 'testitem'

    dataset = db.Column(db.String(32), primary_key=True)
    item = db.Column(db.String(100), primary_key=True)
    status = db.Column(db.String(15))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TestItemSchema(ma.ModelSchema):
    class Meta:

        model = TestItem
        sqla_session = db.session
