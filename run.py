from flask import Flask
from app.api.blueprint import party
from app.api.blueprint import office
app=Flask(__name__)
app.register_blueprint(party)  #register party blueprint
app.register_blueprint(office)

if __name__ == '__main__':
    app.run(debug =True)
