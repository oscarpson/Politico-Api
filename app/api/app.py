from flask import Flask
from app.api.blueprint import party
from app.api.blueprint import office
def create_app():    
    app=Flask(__name__)
    app.register_blueprint(party)  #register party blueprint
    app.register_blueprint(office)
    return app