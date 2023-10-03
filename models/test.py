from db import db


class TestModel(db.Model):
    __tablename__ = "tests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)