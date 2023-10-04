import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from db import db

import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint

from resources.user import blp as UserBlueprint
from resources.test import blp as TestBlueprint
from resources.map import blp as MapBlueprint
from resources.path import blp as PathBlueprint



def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # 初始化DB物件
    db.init_app(app)
    migrate = Migrate(app, db)  # 取代下兩行建立DB
    # with app.app_context():
    #     db.create_all()

    # 初始化API
    api = Api(app)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)   
    api.register_blueprint(UserBlueprint) 
    api.register_blueprint(TestBlueprint)
    api.register_blueprint(MapBlueprint)
    api.register_blueprint(PathBlueprint)
  
    
    return app



