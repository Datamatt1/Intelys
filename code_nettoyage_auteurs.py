import pandas as pd

df = pd.read_csv("Intelys/auteurs.csv")

# --- Affichages de vérification initiale ---
print("Colonnes :", df.columns.tolist())
print(f"Nombre de lignes au départ : {len(df)}")

# --- Compter les doublons avant suppression ---
nombre_doublons = df.duplicated().sum()
print(f"Nombre de doublons détectés : {nombre_doublons}")

# --- Remplacer les cases vides par une valeur ---
# -1 = année inconnue ou auteur encore en vie
df["annee_naissance"] = df["annee_naissance"].fillna(-1)
df["annee_deces"] = df["annee_deces"].fillna(-1)

# --- Supprimer les doublons ---
df = df.drop_duplicates()

# --- Convertir les années en nombres entiers ---
df["annee_naissance"] = df["annee_naissance"].astype(int)
df["annee_deces"] = df["annee_deces"].astype(int)

# --- Sauvegarder le fichier nettoyé ---
df.to_csv("Intelys/auteurs_nettoye.csv", index=False)

# --- Résultat final ---
print(f"Nombre de lignes après nettoyage : {len(df)}")
print(f"{nombre_doublons} lignes doublonnées supprimées")
