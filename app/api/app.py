from flask import Flask
from flask_jwt_extended import (JWTManager)
from app.instance.config import app_config
from app.api.blueprintv2 import party
from app.api.blueprintv2 import office as v2office
from app.api.blueprintv2 import user as usr
from app.api.blueprintv2 import vote as voter
from app.api.blueprint import *
from app.database.createTable import CreateTables as createtb


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
    jwt = JWTManager(app)
    app.register_blueprint(party)  #register party blueprint
    app.register_blueprint(v2office)
    #app.register_blueprint(v1office)
    app.register_blueprint(usr)
    app.register_blueprint(voter)

    createdbInstance = createtb()
    createdbInstance.tables()
    return app