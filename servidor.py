from flask import Flask,request
from flask_socketio import SocketIO, send
from funciones import BD

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def hello_world():

    return 'Hello from Flask xd!'


@app.route('/verTienda', methods=["GET"])
def verTienda():

    bd = BD()
    return bd.verTienda()



if __name__ == "__main__":
    app_flask = app
    app_flask.run(debug=True,host="0.0.0.0")



