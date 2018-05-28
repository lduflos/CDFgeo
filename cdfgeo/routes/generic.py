from flask import render_template, request, flash, redirect
from ..app import app

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

