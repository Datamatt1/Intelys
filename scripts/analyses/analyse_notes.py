import pandas as pd
import matplotlib.pyplot as plt


notes=pd.read_csv("data/sources/notes.csv")

print(notes.columns)
print(notes.describe())

print(f"Nombre de notes non renseignées: {notes["note"].isna().sum()}")     ##### Toutes les notes sont renseignées
print(f"Nombre de work_id non renseignés: {notes["work_id"].isna().sum()}")  ## Tous les work_id sont renseignés
print(f"Nombre de dates non renseignées: {notes["date"].isna().sum()}")  ###Toutes les dates sont renseignées
print(f'Type de la colonne "note": {(notes["note"].dtype)}')   ### Toutes les valeurs sont des entiers
print(f"Note moyenne: {notes["note"].mean().round(2)}")  ## Note moyenne de 4.01
print(f"Nombre de work_id différents: {notes["work_id"].unique().size}")  ### 45427 work ID différents
print(notes.groupby("work_id").agg(note_moyenne=("note", "mean")))

repartition_notes=notes.groupby("note").agg(Nombre_de_notes=("note", "count"))
print(repartition_notes)


fig, ax = plt.subplots()
barres_notes=ax.bar(repartition_notes.index, repartition_notes["Nombre_de_notes"])
ax.set(title="Repartition des notes", xlabel="Note", ylabel="Nombre")
plt.show()

