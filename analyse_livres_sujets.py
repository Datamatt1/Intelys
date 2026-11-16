import pandas as pd
df = pd.read_csv("livres_sujets.csv")
print(df.shape)
print(df.head())
print(f"Doublons: {df.duplicated().sum()}")
print(f"Valeurs manquantes: \n{df.isna().sum()}")
