import pandas as pd

# Defina o nome do arquivo CSV
csv_file = "dados.csv"

# Função para verificar se a combinação CD_CONTA_CONTABIL e REG_ANS é única
def verifica_chave_composta():
    df = pd.read_csv(csv_file, sep=';', engine='python', encoding='utf-8')
    
    if 'CD_CONTA_CONTABIL' not in df.columns or 'REG_ANS' not in df.columns:
        print("As colunas necessárias não existem no arquivo CSV.")
        return
    
    duplicados = df.duplicated(subset=['CD_CONTA_CONTABIL', 'REG_ANS']).sum()
    
    if duplicados > 0:
        print(f"Foram encontradas {duplicados} repetições da combinação CD_CONTA_CONTABIL + REG_ANS.")
    else:
        print("A combinação CD_CONTA_CONTABIL + REG_ANS é única na tabela.")

# Executa a verificação
verifica_chave_composta()
