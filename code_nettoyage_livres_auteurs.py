import pandas as pd


df = pd.read_csv("livres_auteurs.csv")

#  Affichages de vérification initiale 
print("Colonnes :", df.columns.tolist())
print(f"Nombre de lignes au départ : {len(df)}")

# Compter les doublons AVANT suppression
# duplicated() renvoie True pour chaque ligne qui est un doublon
nombre_doublons = df.duplicated().sum()
print(f"Nombre de doublons détectés : {nombre_doublons}")

# Supprimer les doublons 
df = df.drop_duplicates()

#  Sauvegarder le fichier nettoyé 
df.to_csv("livres_auteurs_nettoye.csv", index=False)


print(f"Nombre de lignes après nettoyage : {len(df)}")
print(f"{nombre_doublons} lignes doublonnées supprimées")
