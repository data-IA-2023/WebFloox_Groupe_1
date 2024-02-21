import pandas as pd 
from sqlalchemy import create_engine, text
import os 
import dotenv




def execute_sql_query(request):
    # Charger les variables d'environnement
    dotenv.load_dotenv()

    # Connexion à la base de données
    DATABASE_URI = os.environ['DATABASE_URI']
    engine = create_engine(DATABASE_URI)

    # Créer une connexion à la base de données
    with engine.connect() as connection:
        # Commencer une transactions
        with connection.begin():
            # Exécuter la requête SQL
            result = connection.execute(text(request))

    # Fermer la connexion
    engine.dispose()

    return result