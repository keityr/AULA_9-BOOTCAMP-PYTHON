import pandas as pd

class CsvProcessador:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        self.df_filtrado = None

    #Definindo a função do filtro
    def filtrar_csv(self, coluna, atributo): 
        df_resetado = self.df.reset_index(drop=True)
        self.df_filtrado = df_resetado[df_resetado[coluna] == atributo]
        return self.df_filtrado

    #Definindo a função do filtro depois do primeiro filtro
    def subfiltro_csv(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]

#Atribuindo os parâmetros dos arquivos
arquivo_csv = 'exemplo.csv'
filtro = 'Cidade'
limite = 'Niteroi'

filtro2 = 'Preco'
limite2 = 200.00

#Processando os arquivos CSV
arquivo_CSV = CsvProcessador(arquivo_csv)


print(arquivo_CSV.filtrar_csv(filtro, limite))
print(arquivo_CSV.subfiltro_csv(filtro2, limite2))



# arquivo_csv2 = 'exemplo2.csv'
# filtro2= 'Preco'
# limite2 = 200.00


#arquivo_CSV2= CsvProcessador(arquivo_csv2)






#print(arquivo_CSV2.filtrar_csv(filtro2, limite2))
