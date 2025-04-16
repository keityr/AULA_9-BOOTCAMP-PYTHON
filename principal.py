import pandas as pd

try:
    class LeitorArquivo:

        def __init__(self, caminho_arquivo: str):
            self.caminho = caminho_arquivo
            self.df = None


        def ler_csv(self, caminho_arquivo): 
            self.df = pd.read_csv(caminho_arquivo)
            return self.df


        def ler_excel(self, caminho_arquivo):
            self.df = pd.read_excel(caminho_arquivo)
            return self.df


    arquivo_csv = 'vendas.csv'
    arquivo_CSV = LeitorArquivo(arquivo_csv)

    arquivo_xlsx = 'vendas.xlsx'
    arquivo_XLSX = LeitorArquivo(arquivo_xlsx)

except Exception as e:

    print(e)


try:

    arquivo_CSV.ler_csv(arquivo_csv)

except FileNotFoundError as e:
    print(e)

try:
    arquivo_XLSX.ler_excel(arquivo_xlsx)

except FileNotFoundError as e:
    print(e)
    
