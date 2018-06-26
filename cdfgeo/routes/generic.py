from flask import render_template, jsonify, request, flash, redirect
from ..app import app
from ..modeles.donnees import Pays
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
    """ Route pour affcher les informations générale sur l'application
    """
    return render_template("pages/a_propos.html")
  
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
    try:
        query = Pays.query.get(pays_id)
        return jsonify(query.pays_to_json())
    except:
        return Json_404()

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

