from .. app import db

# A la fin de la phase test, penser à remettre l'auto-incrémentation pour les id !

##############################################################################################################
#                                                 CHAIRE                                                     #
##############################################################################################################

class Chaire(db.Model):
    __tablename__ = "chaire"
    chaire_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    chaire_intitule = db.Column(db.Text)
    chaire_type = db.Column(db.Text)
    chaire_debut = db.Column(db.String(4))
    chaire_fin = db.Column(db.String(4))
    chaire_precision = db.Column(db.Text)
    # Jointure
    personnes = db.relationship("Personne", uselist=False, back_populates="chaire")


##############################################################################################################
#                                                 PERSONNE                                                   #
##############################################################################################################

class Personne(db.Model):
    __tablename__ = "personne"
    personne_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    personne_prenom = db.Column(db.Text)
    personne_nom = db.Column(db.Text)
    personne_statut = db.Column(db.Text)
    personne_naissance = db.Column(db.String(4))
    personne_deces = db.Column(db.String(4))
    personne_precision = db.Column(db.Text)
    personne_liensexternes = db.Column(db.Text)
    chaire_chaire_id = db.Column(db.Integer, db.ForeignKey('chaire.chaire_id'))
    # Jointures
    chaire = db.relationship("Chaire", back_populates="personnes")
    missions = db.relationship("Personne_Mission", back_populates="personne")


##############################################################################################################
#                                              VILLES                                                        #
##############################################################################################################

class Ville(db.Model):
    __tablename__ = "ville"
    ville_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    ville_intitule = db.Column(db.Text)
    ville_lat = db.Column(db.Float)
    ville_long = db.Column(db.Float)
    # Jointure
    missions = db.relationship("Mission_Lieu", back_populates="ville")


##############################################################################################################
#                                              PAYS                                                          #
##############################################################################################################

class Pays(db.Model):
    __tablename__ = "pays"
    pays_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    pays_intitule = db.Column(db.Text)
    pays_lat = db.Column(db.Float)
    pays_long = db.Column(db.Float)
    # Jointure
    missions = db.relationship("Mission_Lieu", back_populates="pays")

    def pays_to_json(self):
        return {
            "type": "Pays",
            "id": self.pays_id,
            "attributes": {
                "nom": self.pays_intitule,
                "longitude": self.pays_long,
                "latitude": self.pays_lat
            },
            "mission": [
                lieu_mission.mission.mission_intitule
                for lieu_mission in self.missions
            ]
        }

##############################################################################################################
#                                                   MISSION                                                  #
##############################################################################################################


class Mission(db.Model):
    __tablename__ = "mission"
    mission_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    mission_intitule = db.Column(db.Text)
    mission_type = db.Column(db.Text)
    mission_institution = db.Column(db.Text)
    mission_date_debut = db.Column(db.String(10))
    mission_date_fin = db.Column(db.String(10))
    mission_dates = db.Column(db.Text)
    mission_precision = db.Column(db.Text)
    # Jointures
    personnes = db.relationship("Personne_Mission", back_populates="mission")
    lieux = db.relationship("Mission_Lieu", back_populates="mission")


##############################################################################################################
#                                                PERSONNE_MISSION                                            #
##############################################################################################################
class Personne_Mission(db.Model):
    __tablename__ = "personne_mission"
    personne_mission_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    personne_mission_personne_id = db.Column(db.Integer, db.ForeignKey('personne.personne_id'))
    personne_mission_mission_id = db.Column(db.Integer, db.ForeignKey('mission.mission_id'))
    # Jointures
    personne = db.relationship("Personne", back_populates="missions")
    mission = db.relationship("Mission", back_populates="personnes")


##############################################################################################################
#                                                 MISSION_LIEU                                               #
##############################################################################################################
class Mission_Lieu(db.Model):
    __tablename__ = "mission_lieu"
    mission_lieu_id = db.Column(db.Integer, nullable=True, autoincrement=True, primary_key=True)
    mission_lieu_mission_id = db.Column(db.Integer, db.ForeignKey('mission.mission_id'))
    mission_lieu_ville_id = db.Column(db.Integer, db.ForeignKey('ville.ville_id'))
    mission_lieu_pays_id = db.Column(db.Integer, db.ForeignKey('pays.pays_id'))
    # Jointures
    ville = db.relationship("Ville", back_populates="missions")
    pays = db.relationship("Pays", back_populates="missions")
    mission = db.relationship("Mission", back_populates="lieux")
