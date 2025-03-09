import sys
import os
from dotenv import load_dotenv

# Charger le fichier .env
load_dotenv()
# ✅ Ajoute le chemin de `app/` pour éviter l'import error
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import create_engine
from alembic import context
from app.models.model_user import Base  # ✅ Assure-toi que `Base` est bien défini dans `models.py`

import time

# 🔄 Teste si Render charge bien DATABASE_URL
print(f"✅ [DEBUG] DATABASE_URL au démarrage : {os.getenv('DATABASE_URL')}")

DATABASE_URL=os.getenv('DATABASE_URL')

DATABASE_URL_SYNC = DATABASE_URL.replace("asyncpg", "psycopg2")

# ✅ Création d'un moteur de connexion synchrone pour Alembic
engine = create_engine(DATABASE_URL_SYNC)

# ✅ Metadonnées pour les migrations (obligatoire pour `--autogenerate`)
target_metadata = Base.metadata

def run_migrations_offline():
    """Exécute les migrations en mode offline."""
    context.configure(url=DATABASE_URL_SYNC, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Exécute les migrations en mode online."""
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
