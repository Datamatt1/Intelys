import pandas as pd

auteurs=pd.read_csv("auteurs.csv")

print(auteurs)
print(auteurs.columns)
print(f"Nombre d'auteurs non renseignés: {auteurs["author_id"].isna().sum()}")
print(f"Nombre de noms non renseignés: {auteurs["nom"].isna().sum()}")
print(f"Nombre d'années de naissance non renseignées: {auteurs["annee_naissance"].isna().sum()}")
print(f"Nombre d'années de décès non renseignées: {auteurs["annee_deces"].isna().sum()}")



print(f"Nombre d'auteurs: {auteurs["author_id"].unique().size}")
print(f"Nombre d'auteurs(colonne nom): {auteurs["nom"].unique().size}")


auteurs_nettoye=auteurs.dropna(subset="nom")

print(auteurs_nettoye["nom"].isna().sum())