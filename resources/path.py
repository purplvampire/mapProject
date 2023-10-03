from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError


from db import db
from models import PathModel, MapModel
from schemas import PathSchema


blp = Blueprint("Pathes", "pathes", description="Operations on pathes")

@blp.route("/map/<string:map_id>/path")
class Path(MethodView):
    # 取得特定路徑
    @blp.response(200, PathSchema(many=True))
    def get(self, map_id):
        map = MapModel.query.get_or_404(map_id)
        return map.pathes.all()

    # 刪除特定路徑
    # def delete(self, map_id):
    #     path = PathModel.query.get_or_404(map_id)
    #     db.session.delete(path)
    #     db.session.commit()
    #     return {"message": "Path deleted."}, 200
        # raise NotImplementedError("Deleting a item is not implemented.")


@blp.route("/path")
class PathList(MethodView):
    # 查所有路徑
    @blp.response(200, PathSchema(many=True))   # 建立清單的回應
    def get(self):
        return PathModel.query.all()
        # raise NotImplementedError("Listing items is not implemented.")

    # 建立新路徑
    @blp.arguments(PathSchema)
    @blp.response(201, PathSchema)
    def post(self, path_data):
        path = PathModel(**path_data)
        try:
            db.session.add(path)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the path.")

        return path