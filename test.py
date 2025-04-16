import pandas as pd

df_novo = pd.read_csv("exemplo.csv")

df_filtrado = df_novo[df_novo['Cidade'] == 'São Paulo']

print(df_filtrado)