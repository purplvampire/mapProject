from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# from db import stores
from db import db
from models import StoreModel
from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # 查詢特定店家
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store


    # 刪除店家
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted."}, 200
        # raise NotImplementedError("Delete a store is not implemented.")

@blp.route("/store")
class StoreList(MethodView):
    # 查詢全店家
    @blp.response(200, StoreSchema(many=True))  # 建立清單的回應
    def get(self):
        return StoreModel.query.all()
        # raise NotImplementedError("Listing store is not implemented.")

    # 建立新店家
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:  # 檢查有無觸發unique=True的錯誤
            abort(400, message="A store with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")

        return store