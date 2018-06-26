# CDFgeo : prototype d'une application cartographie 
CDFgeo est une application prototype qui a été développée dans le cadre d'un stage de fin d'étude du master TNAH de l'Ecole des chartes au Collège de France (Chaire de Littérature française moderne et contemporaine). Cet outil cartographique permet la visualisation des déplacements des professeurs du Collège de France entre 1900 et 1950.

Ce document contient l'ensemble des procédures d'installation pour utiliser cette application. 

## Installation 
### OS X / Mac
#### Pré-requis : installation de Python et Mysql
Vous devez avoir installé Python et Mysql sur votre poste.
Avant l’installation de Python, vous devez installer le gestionnaire de paquets HomeBrew (équivalent apt-get sous linux)

Installation de HomeBrew
Pour installer Homebrew, ouvrez le Terminal et exécutez
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)`

Maintenant, nous pouvons installer Python 3:
`brew install python3`

Installation virtualenv
`pip install virtualenv`

Installation Mysql
`brew install mysql`

#### Première utilisation  
Lancez le dossier **cdfgeo** dans un terminal et tapez :  
`virtualenv ~/.cdfgeo -p python3`  
Cela crée un environnement virtuel dans lequel pourront être installés les packages utilisés. Pour activer cet environnement virtuel, tapez :  
`source ~/.cdfgeo/bin/activate`  
*Cette commande sera nécessaire à chaque fois que vous voudrez activer l'environnement virtuel pour utiliser l'application.*  
  
Dans le même terminal, tapez :  
`pip install -r requirements.txt`  
Cela installe les packages requis pour faire fonctionner l'application.  

Pour lancer l'application, tapez :  
`python3 run.py` 

#### Utilisations ultérieures :
Lancez le terminal depuis le dossier principal et entrez :  
`source ~/.cdfgeo/bin/activate`  
puis  
`python3 run.py`


### Linux (Ubuntu/Debian)
#### Pré-requis 
Vous devez avoir installé MySQL sur votre poste. 

#### Première utilisation  
Vous aurez sûrement besoin d'installer **python3**, **virtualenv** et **pip**, pour cela, ouvrez un terminal et tapez :  
`sudo apt-get install python3 python3-pip python3-virtualenv python3-dev libmysqlclient-dev libfreetype6-dev`  
puis :  
`sudo apt install virtualenv`  

Téléchargez le repository de l'application, lancez le dossier **dico-proso/** dans un terminal et tapez :  
`virtualenv ~/.cdfgeo -p python3`  
Cela crée un environnement virtuel dans lequel pourront être installés les packages utilisés. Pour activer cet environnement virtuel, tapez :  
`source ~/.cdfgeo/bin/activate`  
*Cette commande sera nécessaire à chaque fois que vous voudrez activer l'environnement virtuel pour utiliser l'application.*  
  
Dans le même terminal, tapez :  
`pip install -r requirements.txt`  
Cela installe les packages requis pour faire fonctionner l'application.  

Pour lancer l'application, tapez :  
`python3 run.py`  

#### Utilisations ultérieures :
Lancez le terminal depuis le dossier principal et entrez :  
`source ~/.cdfgeo/bin/activate`  
puis  
`python3 run.py`  

  
## Creation de la base de données "cdfgeo"
Vous pouvez trouver dans le dossier 'modele_db' le fichier "modele_db.sql". 

Prérequis pour créer la base de données :
MySQL installé sur votre ordinateur
accès administrateur à cette base de données

En utilisant MySQL Workbench, copiez le contenu du fichier "modele_db.sql" et exécutez-le. La base est installée. Si elle n'apparait pas dans le menu de gauche, faites "refresh". Pour insérer les données, copiez le contenu du fichier "sample_data_test.sql" et exécutez-le

ou 

dans le terminal (remplacer xxx par le chemin du repertoire ou se trouve le fichier sql.)  
mysql -uroot -p < xxxx/modele_db.sql  
mysql -uroot -p < xxxx/sample_data_test.sql
