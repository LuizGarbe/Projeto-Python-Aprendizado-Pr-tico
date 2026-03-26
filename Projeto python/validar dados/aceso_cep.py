import requests

class BuscarEnderreco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido")
    
    def __str__(self):
        return self.format_cep
        
    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return " {}-{}".format(self.cep[:5], self.cep[5:])
    
    def acessa_cep (self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        resposta = r.json()
        return (
            resposta['bairro'],
            resposta['localidade'],
            resposta['cep'],
            resposta['logradouro'],
            resposta['uf'],
            resposta['ddd']
        )
    
cep = "05081060"
objeto_cep = BuscarEnderreco(cep)
bairro, localidade, cep, logradouro, uf, ddd = objeto_cep.acessa_cep()
print(bairro, localidade,"Cep", cep,"Rua", logradouro, uf, "ddd", ddd)