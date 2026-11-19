import pandas as pd
# Charger le CVS - texte - cellules vides gardées comme ""
df_original = pd.read_csv("data/sources/livres_sujets.csv", dtype=str, keep_default_na=False)

# Copie
df_livres_sujets = df_original.copy()

# Nettoyage de la colonne sujet:

df_livres_sujets["sujet"] = (
    df_livres_sujets["sujet"]
    .str.strip() # supprimer espaces au début et à la fin
    .str.lower() #minuscules
    .str.replace(r"\s+", " ", regex=True) #Remplacer les espaces multiples
    .str.replace(r"[^\w\s]", " ", regex=True)) #Remplacer la ponctuation par un espace
df_livres_sujets = df_livres_sujets[df_livres_sujets["sujet"] != ""].copy()


print(df_livres_sujets.shape)
print(f"\n{df_livres_sujets.head()}")

# Valeurs manquantes
print(f"\nValeurs manquantes: \n{(df_livres_sujets == "").sum()}")

# Doublons après nettoyage
print(f"\nDoublons: {df_livres_sujets.duplicated(["work_id", "sujet"], keep=False).sum()}") #False : Marquer tous les doublons comme True


# Sujets avant et après nettoyage
sujets_avant = df_original["sujet"].nunique()
sujets = df_livres_sujets["sujet"].nunique()
id = df_livres_sujets["work_id"].nunique()

print(f"\nSujets uniques avant: {sujets_avant}")
print(f"Sujets uniques après: {sujets}")
print(f"Id uniques: {id}")

print(f"\n{df_livres_sujets["sujet"].value_counts().head(15)}")
sujets_par_livre = df_livres_sujets.groupby("work_id")["sujet"].agg(list)
print(sujets_par_livre.iloc[0])

print(df_livres_sujets.dtypes)


df_livres_sujets.to_csv("data/nettoyees/livre_sujet_propre.csv", index=False)
livre_sujet_propre=pd.read_csv("data/nettoyees/livre_sujet_propre.csv")
print(livre_sujet_propre)