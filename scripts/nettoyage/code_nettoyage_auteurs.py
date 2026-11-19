import pandas as pd

df = pd.read_csv("data/sources/auteurs.csv")

#Remplacer les cases vides par une valeur simple
df["annee_naissance"] = df["annee_naissance"].fillna(-1)  # -1 = annÃ©e inconnue
df["annee_deces"] = df["annee_deces"].fillna(-1)          # -1 = vivant ou inconnu

#Supprimer les doublons seulement !!
df = df.drop_duplicates()

#Mettre en nombre
df["annee_naissance"] = df["annee_naissance"].astype(int)
df["annee_deces"] = df["annee_deces"].astype(int)

df.to_csv("data/nettoyees/auteurs_nettoye.csv", index=False)



