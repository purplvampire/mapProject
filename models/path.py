from db import db


class PathModel(db.Model):
    __tablename__ = "pathes"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(precision=15), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=15), unique=False, nullable=False)
    map_id = db.Column(
        db.Integer, db.ForeignKey("maps.id"), unique=False, nullable=False
    )
    # 建立多對一關聯
    map = db.relationship("MapModel", back_populates="pathes")
    # 建立多對多關聯
    # tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
