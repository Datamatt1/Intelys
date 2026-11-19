import pandas as pd

auteurs_nettoye=pd.read_csv("auteurs_nettoye.csv")
livres_auteurs_nettoye=pd.read_csv("livres_auteurs_nettoye.csv")
livre_sujet_propre=pd.read_csv("livre_sujet_propre.csv")
livres_propre=pd.read_csv("livres_propre.csv")


livres_complet=livres_propre.merge(livres_auteurs_nettoye, on="work_id",how="left")
livres_complet=livres_complet.merge(auteurs_nettoye,on="author_id",how="left")
livres_complet=livres_complet.merge(livre_sujet_propre,on="work_id",how="left")

print(livres_complet.columns)

print(livres_complet.head())
livres_complet.to_csv("livres_complet.csv", index=False)