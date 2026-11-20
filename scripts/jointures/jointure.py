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
print(livres_complet.columns)
print(livres_complet.head())
print("Nombre de lignes :", len(livres_complet))
print("Nombre de livres uniques :", livres_complet["work_id"].nunique())

# Export
livres_complet.to_csv("data/final/livres_complet.csv", index=False)


# # API de Google Books

# # Charger les variavles du fichier .env
# load_dotenv()

# # Récupérer la clé API
# api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

# if not api_key:
#     raise ValueError("La clé API est introuvable")

# print("Clé API chargée avec succès")



# url_livre = "https://www.googleapis.com/books/v1/volumes" \
# "?q=python"\
# "&orderBy=relevance"\
# "&langRestrict=fr"\
# "&printType=books"\
# f"&key={api_key}"


# def get_content(url):

#     livres = []

#     limit = 40
#     offset = 0

#     while True:

#         reponse = r.get(url, timeout=30)
#         reponse.raise_for_status()                  # Status code est correct

#         data = reponse.json()

#         # Récupérer les informations de chaque livre
#         items = data.get("items", [])

#         if not items:
#             break

#         for item in items:
#             volume_info = item.get("volumeInfo", {})   # volumeInfo contient toutes les informations importantes des livres
#             livres.append(volume_info)

#         # Passer à la page suivante
#         offset += limit

#         # Arrêter lorsque tous les résultats ont été parcourus
#         if offset >= data["totalItems"]:
#             break

#         time.sleep(0.2)
#     return livres

# # Transformer les résultats en DataFrame
# def get_dataframe():
#     lst_livre = get_content(url_livre)
#     df = pd.json_normalize(lst_livre, sep="_")
#     return df

# df_api_book = get_dataframe()

# df_api_book.to_csv("data/final/api_google_book.csv", index=False)


google_book = pd.read_csv("data/final/api_google_book.csv")
print(google_book.head())