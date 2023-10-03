from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

# from db import items
from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint("Items", "items", description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # 刪除商品
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}, 200
        # raise NotImplementedError("Deleting a item is not implemented.")

    # 更新商品資訊
    @blp.arguments(ItemUpdateSchema)    # 將JSON資料Check後傳入item_data
    @blp.response(200, ItemSchema)      # 處理正常回應
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id) # 注意用get,無值時可新增
        # 有值就更新，無值就新增
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item

        # raise NotImplementedError("Updating a item is not implemented.")

@blp.route("/item")
class ItemList(MethodView):
    # 查所有商品
    @blp.response(200, ItemSchema(many=True))   # 建立清單的回應
    def get(self):
        return ItemModel.query.all()
        # raise NotImplementedError("Listing items is not implemented.")

    # 建立新商品
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item