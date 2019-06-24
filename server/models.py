from datetime import datetime, timedelta

from config import db, ma


class Item(db.Model):

    __tablename__ = 'item'

    item = db.Column(db.String(100), primary_key=True)
    status = db.Column(db.String(15), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    dataset_name = db.Column(
        db.String(32), db.ForeignKey('dataset.name'), nullable=False, primary_key=True
    )


class ItemSchema(ma.ModelSchema):
    class Meta:

        model = Item
        sqla_session = db.session


class Dataset(db.Model):

    __tablename__ = 'dataset'

    name = db.Column(db.String(32), primary_key=True)
    datatype = db.Column(db.String(15), nullable=False)
    items = db.relationship('Item', backref='dataset', lazy=True)


class DatasetSchema(ma.ModelSchema):
    class Meta:

        model = Dataset
        sqla_session = db.session


class Settings(db.Model):

    __tablename__ = 'settings'

    use_status = db.Column(db.Boolean, primary_key=True, default=False)
    use_quarantine = db.Column(db.Boolean, default=False)
    timeout = db.Column(db.Interval, default=timedelta(0))


class SettingsSchema(ma.ModelSchema):
    class Meta:

        model = Settings
        sqla_session = db.session
