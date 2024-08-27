from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
import datetime

app = Flask(__name__)

#Inicio de dependencias
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


#Modelos

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


with app.app_context():
    db.create_all()