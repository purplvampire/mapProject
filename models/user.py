from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)        # 密碼不限長度
    image = db.Column(db.Text, nullable=True)  

    # 建立關聯，一但刪除將連鎖刪除items資料
    maps = db.relationship("MapModel", back_populates="user", lazy="dynamic", cascade="all, delete")
      
