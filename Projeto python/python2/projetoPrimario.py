url = ("www.nike.com.br/sc/presentes-nike")
print(url)

url = url.strip()

if url == "":
    raise ValueError("Não possui nenhum atributo")

indice_sc = url.find("/")
url_base = url[:indice_sc]
url_parametros = url[indice_sc+1:]

parametro_busca = "presentes"
indice_parametro = url_parametros.find(parametro_busca)
indice_produto = indice_parametro + len(parametro_busca)+1
indice_traco = url_parametros.find("-", indice_produto)
if indice_traco == -1:
    resultado = url_parametros[indice_produto:]
else:
    resultado = url_parametros[indice_produto: indice_traco]
print(resultado)