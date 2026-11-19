import pandas as pd

df_livre = pd.read_csv("livres.csv")
df_notes = pd.read_csv("notes.csv")

pd.set_option('display.max_columns', None)

# Etape 1: Identifier les colonnes ayant des valeurs null

# 35k valeur null pour l'année de publication
# 16k livre sans résumé
# 4k sans identifiant de couverture
# 3k nb_page_median 
# 3.5k sans note moyenne
# 2k livres sans langues précisées

colonne_null = df_livre.isna().sum()




# nb_veut_lire, nb_en_cours, nb_deja_lu : nb utilisateur ayant classé le lire 'à lire', 'en cours', 'lu'

# Etape 2 : Exploration des données

# A. Identifier les livres les plus recommandés
df_livre = df_livre.sort_values("nb_veut_lire", ascending=False)

top_livre = df_livre[["titre", "nb_veut_lire", "nb_lecteurs", "note_moyenne"]].head()
# print(top_livre)

# B. Nombre de livre disponibles en français
# print(df_livre["disponible_fr"].value_counts())

# C. Les livres avec le plus d'édition
plus_edition = df_livre.sort_values("nb_editions", ascending=False).head(20)
# print(plus_edition[["titre", "nb_editions", "nb_veut_lire", "nb_lecteurs", "note_moyenne"]])




# Etape 3 : Nettoyage de la table
# A. Conserver uniquement les livres FR
livre_fr = df_livre["disponible_fr"] == 1
df_livre = df_livre[livre_fr]

# B. Ajouter la valeur sans sous-titre au None
df_livre["sous_titre"] = df_livre["sous_titre"].fillna("Absent")


# C. Changer le format des titres
df_livre["titre"] = df_livre["titre"].str.strip().str.capitalize()


# D. Supprimer des colonnes
df_livre = df_livre.drop(columns=["nb_editions", "langues", "nb_veut_lire", "nb_en_cours", "nb_deja_lu"])



df_livre.to_csv("livres_propre.csv", index=False)
livres_propre=pd.read_csv("livres_propre.csv")
print(livres_propre)
# API google book : Liste des livres manquants

