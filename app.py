from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from flask_socketio import SocketIO # type: ignore

app = Flask(__name__)
CORS(app)  # Habilitar CORS
socketio = SocketIO(app)

@app.route('/')
def hello():
    return "¡Hola, mundo!"

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

if __name__ == "__main__":
    socketio.run(app, debug=True)
