# Esse repositório é para um teste de processo seletivo da intuitive Care

## Desafio1:
#WebScraping, criar um script que acesse um link de um site e baixe dois arquivos pdf
#Qual linguagem?
Linguagem: Python

### O que pensei? Como foi feito?
Pegar o html pelo 'request' como string 
criar uma lista de tag links, usando o 're', expressão regular de '<a*a/>'
filtrar as tags que continham os nomes dos arquivos pedidos
dessas tags pegar o link, pelo 'href*', depois desses links pegar todos que é .pdf para ter certeza
baixar os itens dos links, depois juntar tudo em um arquivo zip 

## **Desafio 2: Extração e Consolidação de Tabelas de PDF**  

**Objetivo:**  
Extrair tabelas de um arquivo PDF (páginas 3 a 180), consolidar os dados em um DataFrame, processá-los e gerar um arquivo CSV compactado em ZIP.  

---  

#### **Linguagem e Pacotes:**  
- **Linguagem:** Python  
- **Pacotes Instalados:**  
  ```bash  
  pip install tabula-py pandas  # Instalação via terminal  

    tabula-py: Extrai tabelas de PDFs.

    pandas: Manipula e concatena DataFrames.

    os (nativo): Remove arquivos temporários.

    zipfile (nativo): Compacta o CSV final.

Passo a Passo:

    Extrair Tabelas:
    python
    Copy

    import tabula  
    paginas = range(3, 181)  # Páginas 3 a 180  
    lista_tabelas = []  
    for page in paginas:  
        tables = tabula.read_pdf(caminho_pdf, pages=page, multiple_tables=True)  
        if tables:  
            lista_tabelas.extend(tables)  

    Processar Dados:

        Padronizar colunas usando a primeira tabela como referência:
        python
        Copy

        colunas_referencia = lista_tabelas[0].columns  
        dataframes_processados = [tabela.reindex(columns=colunas_referencia) for tabela in lista_tabelas]  

        Substituir valores nulos por None:
        python
        Copy

        df_final = df_final.where(pd.notnull(df_final), None)  

        Renomear colunas OD e AMB:
        python
        Copy

        df_final.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)  

    Gerar CSV e ZIP:
    python
    Copy

    df_final.to_csv('dados_consolidados.csv', index=False)  
    with zipfile.ZipFile("Teste_Davi.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:  
        zipf.write('dados_consolidados.csv')  
    os.remove('dados_consolidados.csv')  # Remove o CSV após compactar  

Problemas Encontrados:

    Páginas 1-2 sem tabelas: Extração iniciou na página 3.

## Desafio 3
**Objetivo:**  
CRIAR TABELAS QUE COMPORTEMA  ESTRUTURA DE CSVs
---  
#### **Linguagem e Pacotes:**  
python -> pandas, 
sql

### O que pensei? Como foi feito?
Idenficar tipos dos campos
Identificar possíveis chaves primárias, no caso criei um scrip para checar repetição, tinha uma ideia pelos nomes que REG_ANS era a chave da primeira tabela, mas queria ver se não se repetia, já a segunda todos os campos minimamente viáveis para serem chave primária se repetiam, então eu fiz uma chave primária composta.
Identificar chave estrangeira Registro_ANS

Criar script de criação de tabelas
task3e4/files/create_table1.sql
task3e4/files/create_table12.sql

Depois de modelado, usar copy para dar insert nas tabelas, delimitador ';'
query1 ->
query2 ->









