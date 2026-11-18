import pandas as pd

df = pd.read_csv("livres_auteurs.csv")

# affichage pour vérifier
print("Colonnes :", df.columns.tolist())
print(f"Lignes avant nettoyage : {len(df)}")

# Supprimer seulement les doublons
df = df.drop_duplicates()

# Sauvegarder et afficher
df.to_csv("livres_auteurs_nettoye.csv", index=False)

print(f"Lignes conservées : {len(df)}")
