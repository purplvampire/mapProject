from db import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), unique=False, nullable=False)
    # 建立關聯，一但刪除將連鎖刪除items資料
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic", cascade="all, delete")