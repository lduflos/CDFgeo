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
    """
    :return """

    missions = Mission.query.all()

    data = dict()
    for mission in missions:
        lieu=mission.missions(data)

    print(lieu)

    return render_template("test_affichage.html", lieu=lieu)


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

