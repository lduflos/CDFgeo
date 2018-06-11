from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask(
    __name__,
    template_folder=templates,
    static_folder=statics
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cdfgeo_user:password@localhost/CDFgeo'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from .routes import generic
