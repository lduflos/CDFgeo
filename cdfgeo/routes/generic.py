from flask import render_template, jsonify, request
from ..app import app
from ..modeles.donnees import Mission, Pays
#############################################################################
#                             PAGES ACCUEIL                                  #
#############################################################################
@app.route("/")
def accueil():
    """ Route permettant l'affichage de la page d'accueil
    """
    return render_template("conteneur.html")

@app.route("/a-propos")
def a_propos():
    """ Route pour afficher les informations générales sur l'application
    """
    return render_template("pages/a_propos.html")
  
@app.route("/test_affichage")
def missions():
    """ Route qui récupère les missions et les affiche sur une carte
    """

    missions = Mission.query.all()

    data = dict()
    for mission in missions:
        lieu=mission.missions(data)

    return render_template("test_affichage.html", lieu=lieu)

@app.route("/pays/<pays_id>")
def _recup_json(pays_id):
    """ Route qui récupère les données des pays en json
    """
    pays = Pays.query.get_or_404(pays_id)
    return jsonify(pays.pays_to_json())

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

