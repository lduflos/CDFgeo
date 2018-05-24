from .. app import db

# A la fin de la phase test, penser à remettre l'auto-incrémentation pour les id !

##############################################################################################################
#                                                 CHAIRE                                                     #
##############################################################################################################

class Chaire(db.Model):
	__tablename__ = "chaire"
	chaire_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
	chaire_intitule = db.Column(db.Tinytext)
	chaire_type = db.Column(db.Tinytext)
	chaire_debut = db.Column(db.String(4))
	chaire_fin = db.Column(db.String(4))
	chaire_precision = db.Column(db.Text)
	# Jointure
	chaire_personne = relationship("Personne", uselist=False, back_populates="personne_chaire")


##############################################################################################################
#                                                 PERSONNE                                                   #
##############################################################################################################

class Personne(db.Model):
	__tablename__ = "personne"
	personne_id = db.Column (db.Integer, unique=True, nullable=False, primary_key=True)
	personne_prenom = db.Column (db.Tinytext)
	personne_nom = db.Column (db.Tinytext)
	personne_statut = db.Column (db.Tinytext)
	personne_naissance = db.Column(db.String(4))
	personne_deces = db.Column(db.String(4))
	personne_precision = db.Column(db.Text)
	personne_liensexternes = db.Column(db.Tinytext)
	chaire_chaire_id = db.Column(db.Integer, db.ForeignKey('chaire.chaire_id'))
	# Jointures 
	personne_chaire = relationship("Chaire", back_populates="chaire_personne")
	personne_mission = relationship("Personne_Mission", back_populates="lien_personne_mission")


##############################################################################################################
#                                                   LIEU                                                     #
##############################################################################################################

class Lieu(db.Model):
	__tablename__ = "lieu"
	lieu_id = db.Column (db.Integer, unique=True, nullable=False, primary_key=True)
	lieu_ville = db.Column (db.Tinytext)
	lieu_latville = db.Column (db.Float)
	lieu_longville = db.Column (db.Float)
	lieu_pays = db.Column (db.Tinytext)
	lieu_latpays = db.Column (db.Float)
	lieu_longpays = db.Column (db.Float)
	# Jointure
	lieu_mission = relationship("Mission_Lieu", back_populates="lien_lieu_mission")


##############################################################################################################
#                                                   MISSION                                                  #
##############################################################################################################

class Mission(db.Model):
	__tablename__ = "mission"
	mission_id = db.Column (db.Integer, unique=True, nullable=False, primary_key=True)
	mission_intitule = db.Column(db.Tinytext)
	mission_type = db.Column(db.Tinytext)
	mission_institution = db.Column(db.Tinytext)
	mission_date_debut = db.Column(db.String(10))
	mission_date_fin = db.Column(db.String(10))
	mission_dates = db.Column(db.Tinytext)
	mission_precision = db.Column(db.Text)
	# Jointures
	mission_personne = relationship("Personne_Mission", back_populates="lien_mission_personne")
	mission_lieu = relationship("Mission_Lieu", back_populates="lien_mission_lieu")


##############################################################################################################
#                                                PERSONNE_MISSION                                            #
##############################################################################################################
class Personne_Mission(db.Model):
    __tablename__ = "personne_mission"
    personne_mission_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    personne_mission_personne_id = db.Column(db.Integer, db.ForeignKey('mission.personne_id'))
    personne_mission_mission_id = db.Column(db.Integer, db.ForeignKey('personne.mission_id'))
	# Jointures
    lien_personne_mission = db.relationship("Personne", back_populates="personne_mission")
    lien_mission_personne = db.relationship("Mission", back_populates="mission_personne")


##############################################################################################################
#                                                 MISSION_LIEU                                               #
##############################################################################################################
class Mission_Lieu(db.Model):
    __tablename__ = "mission_lieu"
    mission_lieu_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    mission_lieu_mission_id = db.Column(db.Integer, db.ForeignKey('lieu.mission_id'))
    mission_lieu_lieu_id = db.Column(db.Integer, db.ForeignKey('lieu.lieu_id'))
	# Jointures
    lien_lieu_mission = db.relationship("Lieu", back_populates="lieu_mission")
    lien_mission_lieu = db.relationship("Mission", back_populates="mission_personne")