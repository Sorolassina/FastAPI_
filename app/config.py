  # Clé API Pappers (remplacez par la vôtre)
PAPPERS_API_KEY = "5c779e5cf0e04a3e814422345db7a29dc311bee60061ebd0"

import os

# 📌 Définir le chemin absolu du projet
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📁 Définir le dossier "fichiers/" pour stocker les PDFs
FICHIERS_DIR = os.path.join(BASE_DIR, "..", "fichiers")

# 📌 S'assurer que le dossier existe
os.makedirs(FICHIERS_DIR, exist_ok=True)


# Dossiers pour stocker les cartes et images
STATIC_MAPS_DIR = "app/static/maps/"
STATIC_IMAGES_DIR = "app/static/images/"
# Créer les dossiers s'ils n'existent pas
os.makedirs(STATIC_MAPS_DIR, exist_ok=True)
os.makedirs(STATIC_IMAGES_DIR, exist_ok=True)


# ✅ Paramètres SMTP pour l'envoi des emails
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "sorolassina58@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # 🔥 Ne PAS mettre le mot de passe en dur !
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT", "lassina.soro.edu@groupe-gema.com")

def get_pdf_path(filename: str) -> str:
    """ Retourne le chemin absolu d'un fichier PDF dans le dossier fichiers/ """
    return os.path.join(FICHIERS_DIR, filename)