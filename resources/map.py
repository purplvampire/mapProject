from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# from db import stores
from db import db
from models import MapModel
from schemas import MapSchema


blp = Blueprint("maps", __name__, description="Operations on maps")

@blp.route("/map/<string:map_id>")
class Map(MethodView):
    # 查詢特定地圖
    @blp.response(200, MapSchema)
    def get(self, map_id):
        map = MapModel.query.get_or_404(map_id)
        return map


    # 刪除地圖
    def delete(self, map_id):
        map = StoreModel.query.get_or_404(map_id)
        db.session.delete(map)
        db.session.commit()
        return {"message": "Map deleted."}, 200
        # raise NotImplementedError("Delete a store is not implemented.")

@blp.route("/map")
class MapList(MethodView):
    # 查詢全地圖
    @blp.response(200, MapSchema(many=True))  # 建立清單的回應
    def get(self):
        return MapModel.query.all()
        # raise NotImplementedError("Listing store is not implemented.")

    # 建立新地圖
    @blp.arguments(MapSchema)
    @blp.response(201, MapSchema)
    def post(self, map_data):
        map = MapModel(**map_data)
        try:
            db.session.add(map)
            db.session.commit()
        except IntegrityError:  # 檢查有無觸發unique=True的錯誤
            abort(400, message="A map with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the map.")

        return map