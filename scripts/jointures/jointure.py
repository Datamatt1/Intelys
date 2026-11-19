import pandas as pd


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