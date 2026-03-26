import re
from typing import Any

class ExtracaoUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL não possui nenhum atributo")
        
        verifica_padrao = re.compile("(http(s)?://)?(www.)?nike.com(.br)?(/sc/)?presentes-nike")
        match = verifica_padrao.match(self.url)
        if not match:
            raise ValueError("A URL não é valida")
        
    def get_url_base(self):
        indice_sc = self.url.find("/")
        url_base = self.url[:indice_sc]
        return url_base
        
    def get_url_parametros(self):
        indice_sc = self.url.find("/")
        url_parametros = self.url[indice_sc+1:]
        return url_parametros
    
    def get_valor_parametros(self, parametro_buscar):
        parametro_buscar = parametro_buscar
        indice_parametro = self.get_url_parametros().find(parametro_buscar)
        indice_produto = indice_parametro + len(parametro_buscar) + 1
        indice_traco = self.get_url_parametros().find("-", indice_produto)
        if indice_traco == -1:
            resultado = self.get_url_parametros()[indice_produto:]
        else:
            resultado = self.get_url_parametros()[indice_produto: indice_traco]
        return resultado
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url
    
    def __eq__(self, other) :
        return self.url == other.url

    def valida_url_base(self, prefixos):
        url_base = self.get_url_base()
        return any (url_base.startswith(prefixo) for prefixo in prefixos)
    
url = ("www.nike.com.br/sc/presentes-nike-200")
extrator_url = ExtracaoUrl(url)

prefixos_validos = ("www.nike.com", "www.adidas.com", "www.youtube.com",)

if extrator_url.valida_url_base(prefixos_validos):
    print("A url base é valida")
else:
    print("A url base não é valida")

#Diferenca de presso dos produtos do Brasil para os USA 
dolar = 5.50
moeda_origem = extrator_url.get_valor_parametros("moedaOrigem")
moeda_destinno = extrator_url.get_valor_parametros("moedaDestino")
quantidade = extrator_url.get_valor_parametros("quantidade")

if moeda_origem == "Real" and moeda_destinno == "Dolar":
    transformar = int(quantidade) / dolar
    print("O valor de R$" + quantidade + "é igual a U$" + str(transformar))
elif moeda_origem == "Dolar" and moeda_destinno == "Real":
    transformar = int(quantidade) * dolar
    print("O valor de U$" + quantidade + "é igual a R$" + str(transformar)) 

valor_quantidade = extrator_url.get_valor_parametros("nike")
print(valor_quantidade)