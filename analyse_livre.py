import pandas as pd
import requests as r
import os
from dotenv import load_dotenv
import time

df_livre = pd.read_csv("livres.csv")
df_notes = pd.read_csv("notes.csv")

pd.set_option('display.max_columns', None)

# Table des livres (Zoubert)

# Etape 1: Identifier les colonnes ayant des valeurs null

colonne_null = df_livre.isna().sum()

# Etape 2 : Exploration des données

# A. Identifier les livres les plus recommandés
df_livre = df_livre.sort_values("nb_veut_lire", ascending=False)

top_livre = df_livre[["titre", "nb_veut_lire", "nb_lecteurs", "note_moyenne"]].head()
# print(top_livre)

# B. Nombre de livre disponibles en français
# print(df_livre["disponible_fr"].value_counts())

# C. Les livres avec le plus d'édition
plus_edition = df_livre.sort_values("nb_editions", ascending=False).head(20)
# print(plus_edition[["titre", "nb_editions", "nb_veut_lire", "nb_lecteurs", "note_moyenne"]])


# Etape 3 : Nettoyage de la table
# A. Conserver uniquement les livres FR
livre_fr = df_livre["disponible_fr"] == 1
df_livre = df_livre[livre_fr]


# B. Ajouter la valeur sans sous-titre au None
df_livre["sous_titre"] = df_livre["sous_titre"].fillna("Absent")


# C. Changer le format des titres
df_livre["titre"] = df_livre["titre"].str.strip().str.capitalize()


# D. Supprimer des colonnes
df_livre = df_livre.drop(columns=["nb_editions", "langues", "nb_veut_lire", "nb_en_cours", "nb_deja_lu"])
 

# Table Luisa
df_original = pd.read_csv("livres_sujets.csv", dtype=str, keep_default_na=False)

# Copie
df_livres_sujets = df_original.copy()

# Nettoyage de la colonne sujet:

df_livres_sujets["sujet"] = (
    df_livres_sujets["sujet"]
    .str.strip() # supprimer espaces au début et à la fin
    .str.lower() #minuscules
    .str.replace(r"\s+", " ", regex=True) #Remplacer les espaces multiples
    .str.replace(r"[^\w\s]", "", regex=True)) #Remplacer la ponctuation par un espace
df_livres_sujets = df_livres_sujets[df_livres_sujets["sujet"] != ""].copy()


# print(df_livres_sujets.shape)
# print(f"\n{df_livres_sujets.head()}")

# # Valeurs manquantes
# print(f"\nValeurs manquantes: \n{(df_livres_sujets == "").sum()}")

# # Doublons après nettoyage
# print(f"\nDoublons: {df_livres_sujets.duplicated(["work_id", "sujet"], keep=False).sum()}") #False : Marquer tous les doublons comme True


# Sujets avant et après nettoyage
sujets_avant = df_original["sujet"].nunique()
sujets = df_livres_sujets["sujet"].nunique()
id = df_livres_sujets["work_id"].nunique()

# print(f"\nSujets uniques avant: {sujets_avant}")
# print(f"Sujets uniques après: {sujets}")
# print(f"Id uniques: {id}")

# print(f"\n{df_livres_sujets["sujet"].value_counts().head(15)}")
sujets_par_livre = df_livres_sujets.groupby("work_id")["sujet"].agg(list)
# print(sujets_par_livre.iloc[0])


# Table Sara
df_auteurs = pd.read_csv("auteurs.csv")

#Remplacer les cases vides par une valeur simple
df_auteurs["annee_naissance"] = df_auteurs["annee_naissance"].fillna(-1)  # -1 = annee inconnue
df_auteurs["annee_deces"] = df_auteurs["annee_deces"].fillna(-1)          # -1 = vivant ou inconnu

#Supprimer les doublons seulement !!
df_auteurs = df_auteurs.drop_duplicates()

#Mettre en nombre
df_auteurs["annee_naissance"] = df_auteurs["annee_naissance"].astype(int)
df_auteurs["annee_deces"] = df_auteurs["annee_deces"].astype(int)




# Sara

df_livres_auteurs = pd.read_csv("livres_auteurs.csv")

# affichage pour vérifier
# print("Colonnes :", df_livres_auteurs.columns.tolist())
# print(f"Lignes avant nettoyage : {len(df_livres_auteurs)}")

# Supprime seulement les doublons
df_livres_auteurs = df_livres_auteurs.drop_duplicates()

# Sauvegarder et afficher
df_livres_auteurs.to_csv("livres_auteurs_nettoye.csv", index=False)



# Table à joindre
# luisa : sujets_par_livre 
# Zoubert : df_livre 
# Sara : df_auteur, df_livre_auteurs 

# Jointure de toutes les tables
df1 = pd.merge(df_auteurs, df_livres_auteurs, how='left', on="author_id")

df = pd.merge(df_livre, sujets_par_livre, how="left", on="work_id")

df = pd.merge(df, df1, how="left", on="work_id")


print(len(df))

# API de Google Books

# Charger les variavles du fichier .env
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

# print(get_dataframe().head())