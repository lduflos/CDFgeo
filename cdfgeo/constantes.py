class _TEST:
    # On configure la base de donnees
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

CONFIG = {
    #"test": _TEST,
    "test": _TEST
}
