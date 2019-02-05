from flask import Flask
from app.api.blueprint import party
app=Flask(__name__)
app.register_blueprint(party)  #register party blueprint

if __name__ == '__main__':
    app.run(debug =True)
