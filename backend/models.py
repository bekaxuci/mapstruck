from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, email, password, name):
        self.email = email
        self.password_hash = generate_password_hash(password)  # Generamos el hash de la contraseña
        self.name = name

    def __repr__(self):
        return f'<User {self.email}>'
