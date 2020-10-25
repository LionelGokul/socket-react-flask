from flask import Flask
from flask_socketio import SocketIO, send
from configSocket import  config

# initializing APP
app = Flask("sample-socket")
app.config['SECRET_KEY'] = 'lionel'

socketIO = SocketIO(app, cors_allowed_origins="*")

app.debug = True

@app.route('/')
def hello_world():
    return 'Hello, World!'

config(socketIO)

if __name__ == '__main__':
    socketIO.run(app)




