from flask import Flask
from flask_socketio import SocketIO, send

# initializing APP
app = Flask("sample-socket")
app.config['SECRET_KEY'] = 'lionel'

socketIO = SocketIO(app, cors_allowed_origins="*")

app.debug = True


@app.route('/')
def hello_world():
    return 'Hello, World!'


@socketIO.on('message', namespace='/api')
def handleMessage(msg):
    send(msg, broadcast=True)
    return None


if __name__ == '__main__':
    socketIO.run(app)




