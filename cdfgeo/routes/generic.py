from flask import render_template, jsonify, request
from ..app import app
from ..modeles.donnees import Pays
#############################################################################
#                             PAGE ACCUEIL                                  #
#############################################################################
@app.route("/")
def accueil():
    """ Route permettant l'affichage de la page d'accueil
    """
    return render_template("conteneur.html")

@app.route("/test_affichage")
def affichage_pays():
    """Route permettant l'affichage de tous les pays de la base
    :return une page html avec une liste"""

    pays = Pays.query.all()
    return render_template("test_affichage.html", pays=pays)

# api
def Json_404():
    response = jsonify({"erreur": "la requête a échoué"})
    response.status_code = 404
    return response

@app.route("/api/pays/<pays_id>")
def api_pays(pays_id):
        query = Pays.query.get(pays_id)
        return jsonify(query.pays_to_json())
    

@app.route("/blop/pays/<pays_id>")
def _recup_json(pays_id) :
    try:
        query = Pays.query.get(pays_id)
        pays = jsonify(query.pays_to_json())
        print("bonjour lea")
        print(pays)
        return render_template("conteneur.html")
    except:
        print("fail")
        return render_template("conteneur.html")

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

