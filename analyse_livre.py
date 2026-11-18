import pandas as pd

df_livre = pd.read_csv("livres.csv")

pd.set_option('display.max_columns', None)

# Etape 1: Identifier les colonnes ayant des valeurs null

# 35k valeur null pour l'année de publication
# 16k livre sans résumé
# 4k sans identifiant de couverture
# 3k nb_page_median 
# 3.5k sans note moyenne
# 2k livres sans langues précisées

colonne_null = df_livre.isna().sum()
print(df_livre.isna().sum())




# nb_veut_lire, nb_en_cours, nb_deja_lu : nb utilisateur ayant classé le lire 'à lire', 'en cours', 'lu'

# Etape 2 : Exploration des données

# A. Identifier les livres les plus recommandés
df_livre = df_livre.sort_values("nb_veut_lire", ascending=False)

top_livre = df_livre[["titre", "nb_veut_lire", "nb_lecteurs", "note_moyenne"]].head()
# print(top_livre)

# B. Nombre de livre disponibles en français
print(df_livre["disponible_fr"].value_counts())

# C. Les livres avec le plus d'édition
plus_edition = df_livre.sort_values("nb_editions", ascending=False).head(10)
# print(plus_edition[["titre", "nb_editions", "nb_veut_lire", "nb_lecteurs", "note_moyenne"]])


print(df_livre)

df_livres_2=df_livre
df_livres_2=df_livres_2[df_livres_2["disponible_fr"]==True]


df_livres_2=df_livres_2.dropna(subset=["resume"])

print(df_livres_2)
print(df_livres_2.isna().sum())

print(df_livres_2.columns)
