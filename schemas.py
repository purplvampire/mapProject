from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# 多對一關聯，避免Loop用
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True) # 多對多的父


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

# 一對多關聯，避免Loop用
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

# 多對一關聯，避免Loop用
class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)               # 一對多的子
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)   # 多對多的父
    # items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)   # 多對多的父

# 多對多關聯的子
class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)

# SocialMap
class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    image = fields.Str()

class PlainMapSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    memo = fields.Str()
    distance = fields.Int()
    path = fields.Str(required=True)
    is_post = fields.Bool()
    post_date = fields.Date()
    post_time = fields.DateTime(required=True)
    period = fields.Str()
    start_time = fields.DateTime()
    end_time = fields.DateTime()

class PlainPathSchema(Schema):
    id = fields.Int(dump_only=True)
    latitude = fields.Float()
    longitude = fields.Float()

# 一對多關聯，避免Loop用
class UserSchema(PlainUserSchema):
    maps = fields.List(fields.Nested(PlainMapSchema()), dump_only=True)

# path:一對多關聯,user:多對一關聯,避免Loop用
class MapSchema(PlainMapSchema):
    user_email = fields.String(required=True, load_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
    pathes = fields.List(fields.Nested(PlainPathSchema()), dump_only=True)

# 多對一關聯，避免Loop用
class PathSchema(PlainPathSchema):
    map_id = fields.Int(required=True, load_only=True)
    map = fields.Nested(PlainMapSchema(), dump_only=True)

class TestSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    