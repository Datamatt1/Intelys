import pandas as pd

livres_auteurs=pd.read_csv("livres_auteurs.csv")
print(livres_auteurs.columns)

print(f"Nombre de work_id non renseignés: {livres_auteurs["work_id"].isna().sum()}")
print(f"Nombre de author_id non renseignés: {livres_auteurs["author_id"].isna().sum()}")
print(f"Nombre d'ordres non renseignés: {livres_auteurs["ordre"].isna().sum()}")

print(livres_auteurs.head())