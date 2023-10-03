from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    # 建立多對一關聯
    store = db.relationship("StoreModel", back_populates="tags")
    # 建立多對多關聯
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")