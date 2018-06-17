from flask import render_template, jsonify, request
from ..app import app
from ..modeles.donnees import Mission
#############################################################################
#                             PAGE ACCUEIL                                  #
#############################################################################
@app.route("/")
def accueil():
    """ Route permettant l'affichage de la page d'accueil
    """
    return render_template("conteneur.html")

@app.route("/test_affichage")
def missions():
    """Route permettant l'affichage de tous les missions de la base
    :return une page html avec une liste"""

    mission = Mission.query.all()
    return render_template("test_affichage.html", mission=mission)


'''
#############################################################################
#                     PAGES DE CONSULTATION DE LA BASE                      #
#############################################################################
@app.route("/recherche")
def recherche():
    """" Route permettant la recherche plein-texte a partir de la navbar
    """


@app.route("/index")
def index():
    """ Route qui affiche la liste des resultats de la base.
    """
    
'''

