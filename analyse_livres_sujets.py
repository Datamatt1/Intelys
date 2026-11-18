import pandas as pd
# Charger le CVS - texte - cellules vides gardées comme ""
df_original = pd.read_csv("livres_sujets.csv", dtype=str, keep_default_na=False)

# Copie
df_livres_sujets = df_original.copy()

# Nettoyage de la colonne sujet:

df_livres_sujets["sujet"] = (
    df_livres_sujets["sujet"]
    .str.lower() # minuscules
    .str.replace(r"\s+", " ", regex=True) # Remplacer les espaces multiples
    .str.strip()) # supprimer espaces au début et à la fin
df_livres_sujets = df_livres_sujets[df_livres_sujets["sujet"] != ""].copy()

# Transformer chaque texte en liste de sujets, séparés par les virgules 
df_livres_sujets["sujet"] = df_livres_sujets["sujet"].str.split(",")
df_livres_sujets = df_livres_sujets.explode("sujet").copy()
df_livres_sujets["sujet"] = df_livres_sujets["sujet"].str.strip()
df_livres_sujets = df_livres_sujets[df_livres_sujets["sujet"] != ""].copy()

# Remplacer la ponctuation par un espace
df_livres_sujets["sujet"] = (
    df_livres_sujets["sujet"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.replace(r"[^\w\s]", " ", regex=True)
)

print(df_livres_sujets.shape)
print(f"\n{df_livres_sujets.head(10)}")

# Valeurs manquantes
print(f"\nValeurs manquantes: \n{(df_livres_sujets == "").sum()}")

# Doublons après nettoyage
print(f"\nDoublons: {df_livres_sujets.duplicated(["work_id", "sujet"], keep=False).sum()}") #False : Marquer tous les doublons comme True

df_livres_sujets = df_livres_sujets.drop_duplicates(["work_id", "sujet"])

# Sujets avant et après nettoyage
sujets_avant = df_original["sujet"].nunique()
sujets = df_livres_sujets["sujet"].nunique()
id = df_livres_sujets["work_id"].nunique()

print(f"\nSujets uniques avant: {sujets_avant}")
print(f"Sujets uniques après: {sujets}")
print(f"Id uniques: {id}")

print(f"\n{df_livres_sujets["sujet"].value_counts().head(10)}")
sujets_par_livre = df_livres_sujets.groupby("work_id")["sujet"].agg(list)
livres_par_sujet = df_livres_sujets.groupby("sujet")["work_id"].agg(list)
print(sujets_par_livre.head())
print(livres_par_sujet.head())
