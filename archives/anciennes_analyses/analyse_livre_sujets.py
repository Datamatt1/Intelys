import pandas as pd

livres_sujets=pd.read_csv("livres_sujets.csv")

print(livres_sujets.columns)
print(livres_sujets.shape)
print(f"Nombre de work_id non renseignés: {livres_sujets["work_id"].isna().sum()}")
print(f"Nombre de sujets non renseignés: {livres_sujets["sujet"].isna().sum()}")
print(f"Nombre de sujets différents: {livres_sujets["sujet"].unique().size}")
print(livres_sujets.describe())

nb_sujet=(livres_sujets.groupby("sujet").agg(Nombre=("sujet", "count")).sort_values("Nombre", ascending=False))
print(nb_sujet.head(10))


nb_sujet.to_csv("livre_sujet_propre.csv")
livre_sujet_propre=pd.read_csv("livre_sujet_propre.csv")
print(livre_sujet_propre)