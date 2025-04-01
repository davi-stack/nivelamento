# Esse repositório é para um teste de processo seletivo da intuitive Care

## Desafio1:
# Como testar?
 Entrar no diretório task1e2
 no linux:
 python3 webscraping1.py
 windows
 python webscraping1.py
 pdfs extraidos na pasta pdfs(se não existir será criado), zip na pasta task1e2

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
# Como testar?
Precisa ter instalar alguns pacotes além do python, abaixo escrevo sobre
então no diretório task1e2 rodar
python3 extract_taable2.py

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
# Como testar?
Baixar os CSVs, do ano  do ano 2023 e 2024 do link https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
e o csv do link https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/
mover para o diretório task3e4, criar um diretório chamado 'files', mover os CVS para dentro deles. Depois no diretório task3e4 rodar o comando python3 remove_virgules.py para remover ',' e trocar por '.', para facilitar o uso dos campos. Após isso, rodar em um banco postgreesql, o scritp de task3e4/create_table1.sql, logo em seguida create_table2.sql. Inserção, rodar extract.sql esse script começa com \copy, pode ser usado apenas copy se for em banco local, eu testei com um remoto. Depois  query1.sql e query2.sql

Há alguns auxiliares que não fazem parte da descrição do desafio, mas foram usados para resolver subproblemas pequenos
task3e4/verity_line.py -> para checar repetições de campo em uma coluna, depois alterei para uma outra para apenas testar uma hipotese de chave primária composta, que de certo
task3e4/check_line_null -> para checar campos em branco
task
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

Problemas Encontrados:
    Campos float usando ',' -> solução: /task3e4/remove_virgules.py

4. **Testando os endpoints:**
   - Acesse `/operadoras?q=TERMO_DE_BUSCA` para buscar operadoras
   - Exemplo:
     ```
     http://localhost:8000/operadoras?q=saude
     ```

**API também disponível em produção:**  
https://nivelamento-5.onrender.com/operadoras?q=TERMO_DE_BUSCA

---

### **Objetivo:**
Criar uma API simples para buscar operadoras de planos de saúde pelos campos Razão Social ou Nome Fantasia.


### **Testes **
Um coleção de testes para essa api está na raiz do projeto em collections_teste.json

### **Linguagem e Pacotes:**
- Python
- FastAPI (framework web)
- uvicorn (servidor ASGI)
- pandas (para manipulação de dados, se necessário)

### **O que pensei? Como foi feito?**
1. **Estrutura da API:**
   - Criei um endpoint GET `/operadoras` que aceita um parâmetro de query `q`
   - Implementei CORS para permitir acesso de qualquer origem

2. **Carregamento de dados:**
   - Função `carregar_operadoras()` lê o CSV e armazena em memória
   - Remove aspas extras e formata os dados

3. **Busca:**
   - Compara o termo de busca (case insensitive) com Razão Social e Nome Fantasia
   - Retorna todas as operadoras que contêm o termo em qualquer um desses campos

4. **Middlewares (comentados):**
   - Implementei (mas deixei comentado) um middleware de autenticação via API Key
   - Pode ser ativado se necessário para controle de acesso

5. **Hospedagem:**
   - Configurei para rodar no Render.com
   - A porta é configurada automaticamente pela variável de ambiente PORT

### **Problemas Encontrados:**
1. **Formato do CSV:**
   - Problema com delimitador ";" e aspas nos campos
   - Solução: Especificar delimitador e remover aspas extras

2. **Case sensitivity:**
   - Busca sensível a maiúsculas/minúsculas
   - Solução: Converter ambos os lados para lowercase

3. **Performance:**
   - Carregar todo o CSV em memória pode ser problemático para arquivos muito grandes
   - Solução atual funciona bem para o tamanho atual do dataset

### **Extras:**
- O código inclui prints de debug (mostrando as 5 primeiras operadoras) que podem ser removidos
- Configuração pronta para deploy em serviços como Render: https://nivelamento-5.onrender.com

# Parte2: front_end: 
   O front-End está hospedado em: https://desafiointuitivecare.vercel.app/
   Código fonte no repositório: https://github.com/davi-stack/desafio_intuitive_care_front











