from pymongo import MongoClient

def get_db():
    # Conexión a MongoDB local
    client = MongoClient('mongodb://localhost:27017/')
    db = client['futbol_db']  # Nombre de la base de datos
    return db
