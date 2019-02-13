from flask import Flask
from app.instance.config import app_config
from app.api.blueprint import party
from app.api.blueprint import office
from app.database.createTable import CreateTables as createtb


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(party)  #register party blueprint
    app.register_blueprint(office)

    createtb().tables()
    return app