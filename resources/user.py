from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# from db import stores
from db import db
from models import UserModel
from schemas import UserSchema # 要改


blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/user/<string:user_id>")
class User(MethodView):
    # 表列某用戶資料
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}, 200

    @blp.arguments(UserSchema)         # 將JSON資料Check後傳入item_data
    @blp.response(200, UserSchema)     # 處理正常回應
    def put(self, user_data, user_id):
        user = UserModel.query.get(user_id)
        # 有值就更新，無值就新增
        if user:
            user.name = user_data["name"]
            user.email = user_data["email"]
            user.password = user_data["password"]
            user.image = user_data["image"]
        else:
            user = UserModel(id=user_id, **user_data)

        db.session.add(user)
        db.session.commit()

        return user
        # raise NotImplementedError("Listing user is not implemented.")

@blp.route("/user/")
class UserList(MethodView):
    # 查所有用戶
    @blp.response(200, UserSchema(many=True))   # 建立清單的回應
    def get(self):
        return UserModel.query.all()
        # raise NotImplementedError("Listing items is not implemented.")

    # 建立用戶
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the user.")

        return user