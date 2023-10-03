from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# from db import stores
from db import db
from models import TestModel
from schemas import TestSchema


blp = Blueprint("tests", __name__, description="Operations on tests")

@blp.route("/test")
class TestList(MethodView):
    # 查詢全店家
    @blp.response(200, TestSchema(many=True))  # 建立清單的回應
    def get(self):
        return TestModel.query.all()
        # raise NotImplementedError("Listing store is not implemented.")

    # 建立新店家
    @blp.arguments(TestSchema)
    @blp.response(201, TestSchema)
    def post(self, test_data):
        test = TestModel(**test_data)
        try:
            db.session.add(test)
            db.session.commit()
        except IntegrityError:  # 檢查有無觸發unique=True的錯誤
            abort(400, message="A store with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")

        return test