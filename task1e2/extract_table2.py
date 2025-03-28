import tabula
import pandas as pd
import os 
import zipfile
# Caminho para o arquivo PDF
caminho_pdf = '../task1/pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

# Páginas a serem extraídas
paginas = range(3, 181)

# Lista para armazenar os DataFrames extraídos
lista_tabelas = []

for page in paginas:
    # Extraindo a tabela da página especificada
    tables = tabula.read_pdf(caminho_pdf, pages=page, multiple_tables=True)
    
    if tables:
        for table in tables:
            lista_tabelas.append(table)

# Verificar se alguma tabela foi extraída
if not lista_tabelas:
    raise ValueError("Nenhuma tabela foi extraída do PDF.")

# Definir as colunas da primeira tabela como referência
colunas_referencia = lista_tabelas[0].columns

# Processar todas as tabelas extraídas
dataframes_processados = []
for tabela in lista_tabelas:
    # Garantir que a tabela possui as colunas de referência
    tabela = tabela.reindex(columns=colunas_referencia)
    dataframes_processados.append(tabela)

# Concatenar todas as tabelas em um único DataFrame
df_final = pd.concat(dataframes_processados, ignore_index=True)

# Substituir valores ausentes por None (null)
df_final = df_final.where(pd.notnull(df_final), None)

# Renomear colunas específicas
df_final.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)

name = 'dados_consolidados.csv'
# Salvar o DataFrame consolidado em um arquivo CSV
df_final.to_csv(name, index=False)

print(f"Arquivo CSV gerado com sucesso: {name}.csv")


with zipfile.ZipFile("Teste_Davi.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(name)

os.remove(name)