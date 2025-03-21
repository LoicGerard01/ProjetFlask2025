from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration de la base de données
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://anonyme:anonyme@localhost/projet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '486ee11b0cf1b50905840952309d18d9'

db = SQLAlchemy(app)

# Importer routes après la création de app et db
from . import routes
