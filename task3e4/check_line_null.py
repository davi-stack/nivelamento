import pandas as pd

# Defina o nome do arquivo CSV
csv_file = "./files/operadoras.csv"


# Função para verificar se uma coluna contém valores nulos
def verifica_null(coluna):
    df = pd.read_csv(csv_file, sep=';', engine='python', encoding='utf-8')
    
    if coluna not in df.columns:
        print(f"A coluna '{coluna}' não existe no arquivo CSV.")
        return
    
    nulos = df[coluna].isnull().sum()
    
    if nulos > 0:
        print(f"A coluna '{coluna}' contém {nulos} valores nulos.")
    else:
        print(f"A coluna '{coluna}' não contém valores nulos.")


