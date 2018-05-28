from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .constantes import CONFIG

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

# On initie l'extension
db = SQLAlchemy()

app = Flask(
    __name__,
    template_folder=templates,
    static_folder=statics
)


from .routes import generic

#repris du modele gazetteer
def config_app(config_name="test"):
    """ Create the application """
    app.config.from_object(CONFIG[config_name])
    app.config['JSON_AS_ASCII'] = False

    # Set up extensions
    db.init_app(app)
    # assets_env = Environment(app)

    # Register Jinja template functions

    return app

