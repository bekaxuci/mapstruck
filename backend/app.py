from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from models import db, User  # Importamos las configuraciones de la base de datos y el modelo User
from werkzeug.security import check_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Cambia a tu base de datos deseada
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos y Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)


# Configuramos CORS para permitir solicitudes del frontend
CORS(app, resources={r"/*": {"origins": "https://probable-space-umbrella-x55765rj7qxj3rjq-3000.app.github.dev"}},
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "OPTIONS"])

# Inicializamos WebSocket
socketio = SocketIO(app, cors_allowed_origins="https://probable-space-umbrella-x55765rj7qxj3rjq-3000.app.github.dev")

@app.route('/')
def hello():
    return "¡Hola, mundo!"

# Ruta de registro
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    # Verificamos si el usuario ya está registrado
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "El usuario ya está registrado"}), 400

    # Creamos el nuevo usuario
    new_user = User(email=email, password_hash=password, name=name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        # Crear token o manejar la sesión del usuario
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401


    

# Evento WebSocket para manejar la conexión
@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

if __name__ == '__main__':
    app.run(debug=True)