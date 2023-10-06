from db import db


class MapModel(db.Model):
    __tablename__ = "maps"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    memo = db.Column(db.String(255), unique=False, nullable=True)
    distance = db.Column(db.Integer)
    path = db.Column(db.Text, nullable=False)
    is_post = db.Column(db.Boolean, unique=False, nullable=True)
    post_date = db.Column(db.Date, unique=False, nullable=True)
    post_time = db.Column(db.DateTime, unique=False, nullable=True)
    period = db.Column(db.Interval, unique=False, nullable=True)
    start_time = db.Column(db.DateTime, unique=False, nullable=True)
    end_time = db.Column(db.DateTime, unique=False, nullable=True)

    user_email = db.Column(
        db.String, db.ForeignKey("users.email"), unique=False, nullable=False
    )
    # 建立多對一關聯
    user = db.relationship("UserModel", back_populates="maps")

    # 建立關聯，一但刪除將連鎖刪除pathes資料
    pathes = db.relationship("PathModel", back_populates="map", lazy="dynamic", cascade="all, delete")
    # tags = db.relationship("TagModel", back_populates="store", lazy="dynamic", cascade="all, delete")