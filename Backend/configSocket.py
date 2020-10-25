from flask_socketio import send

def myfunction(msg):
    send(msg, broadcast=True)
    return None

def config(socketIO):
    socketIO.on_event('message', myfunction, namespace='/api')
