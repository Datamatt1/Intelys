import pandas as pd
import os
import requests as r
from dotenv import load_dotenv
import time


# Chargement des CSV nettoyés
auteurs_nettoye = pd.read_csv("data/nettoyees/auteurs_nettoye.csv")
livres_auteurs_nettoye = pd.read_csv("data/nettoyees/livres_auteurs_nettoye.csv")
livre_sujet_propre = pd.read_csv("data/nettoyees/livre_sujet_propre.csv")
livres_propre = pd.read_csv("data/nettoyees/livres_propre.csv")

# Regrouper uniquement les sujets par livre
sujets_groupes = livre_sujet_propre.groupby("work_id").agg(sujet=("sujet", list)).reset_index()

# Jointures classiques
livres_complet = livres_propre.merge(livres_auteurs_nettoye, on="work_id", how="left")
livres_complet = livres_complet.merge(auteurs_nettoye, on="author_id", how="left")
livres_complet = livres_complet.merge(sujets_groupes, on="work_id", how="left")

# Vérifications
# print(livres_complet.columns)
# print(livres_complet.head())
# print("Nombre de lignes :", len(livres_complet))
# print("Nombre de livres uniques :", livres_complet["work_id"].nunique())

# Export
# livres_complet.to_csv("data/final/livres_complet.csv", index=False)


# API de Google Books

# Charger les variavles du fichier .env
load_dotenv()

# # Récupérer la clé API
api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

# if not api_key:
#     raise ValueError("La clé API est introuvable")


API_URL = "https://www.googleapis.com/books/v1/volumes"

def get_content(query, api_key):
    """Récupère le genre du livre souhaité et la clé API"""

    livres = []
    limit = 40
    offset = 0

    while True:

        params = {
            "q": query,
            "langRestrict": "fr",
            "printType": "books",
            "orderBy": "relevance",
            "maxResults": limit,
            "startIndex": offset,
            "key": api_key
        }

        response = r.get(API_URL, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        items = data.get("items", [])

        if not items:
            break


        # Les information des livres sont dans volumeInfo
        for item in items:
            volume_info = item.get("volumeInfo", {})
            volume_info["google_books_id"] = item.get("id")
            volume_info["search_category"] = query
            livres.append(volume_info)

        offset += len(items)

        if offset >= data.get("totalItems", 0):
            break

        time.sleep(0.2)

    return livres


# Les trois thématiques collectées dans le google book
categories = {
    "Histoire": "subject:history",
    "Livres pratiques": "pratique",
    "Science-fiction": "subject:science fiction"
}

# Collecte
tous_les_livres = []

for categorie, query in categories.items():

    resultats = get_content(query, api_key)
    tous_les_livres.extend(resultats)

    print(f"{categorie} : {len(resultats)} livres récupérés")


# Création du DataFrame
df = pd.json_normalize(tous_les_livres, sep="_")

# Suppression des doublons
df = df.drop_duplicates(
    subset="google_books_id"
).reset_index(drop=True)

print("Total de livres uniques :", len(df))


df.to_csv("data/final/api_google_book.csv", index=False)

a = pd.read_csv("data/final/api_google_book.csv")
print(a.info())