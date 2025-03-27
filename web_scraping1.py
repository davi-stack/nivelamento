import requests
import zipfile
import re
import os

html = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")


# todas as tags <a ... </a>
tags_a = re.findall(r'<a.*?</a>', html.text)
# print(tags_a)
str
tags_a_f = []
for tag in tags_a:
    if "Anexo" in tag:
        tags_a_f.append(tag)

tags_a = tags_a_f
links = []

for tag in tags_a:
    # busca o link
    link = re.search(r'href="(.*?)"', tag)
    if link:
        links.append(link.group(1))

anexos = []
for link in links:
    if link.endswith(".pdf") or link.endswith(".pdf"):
        anexos.append(link)

print(anexos)
#criar uma pasta para os links
if not os.path.isdir("./pdfs"):
    os.mkdir("./pdfs")

for link in anexos:
    print("teste")
    response = requests.get(link, stream=True)
    
    name = link.split("/")
    if len(name) > 0:
        name = name[len(name)-1]
    name = "pdfs/"+name
    if response.status_code==200:
        with open(name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"pdf salvo como: {name}")
    else:
        print(f"Erro ao baixar o arquivo: {name}")
#baixa os anexos


with zipfile.ZipFile("resultado_compactado.pdf", 'w', zipfile.ZIP_DEFLATED) as zipf:
    for raiz, _, files in os.walk("./pdfs"):
        for file in files:
            path = os.path.join(raiz, file)
            path_relativo = os.path.relpath(path, "./pdfs")
            zipf.write(path, path_relativo)

