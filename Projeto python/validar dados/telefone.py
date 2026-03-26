import re

class Telefone:
    def __init__(self, telefone):
        if self.valida_numero(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numeroinvalido ")
    
    def __str__(self):
        return self.format_numero()
    
    def valida_numero(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        reprodusao = re.findall(padrao, telefone)
        if reprodusao:
            return True
        else:
            return False
    
    def format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        reprodusao = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(reprodusao.group(1),reprodusao.group(2), reprodusao.group(3), reprodusao.group(4))
        return numero_formatado

telefone = "5511951733157"
objeto = Telefone(telefone)
print(objeto)