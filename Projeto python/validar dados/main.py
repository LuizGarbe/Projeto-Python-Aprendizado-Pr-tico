# this cod is for learn
from validate_docbr import CPF, CNPJ

class DCocumento:
    @staticmethod
    def cria_doc(docum):
        docstr = str(docum)
        if len(docstr) == 11:
            return docCpf(docstr)
        elif len(docstr) == 14:
            return doccnPj(docstr)
        else:
            raise ValueError ("u")

class docCpf:
    def __init__(self, docum):
        if self.valide(docum):
            self.cpf = docum
        else:
            raise ValueError ("shit")

    def __str__(self) -> str:
        return self.maca()
    
    def valide(self,docum):
        validader = CPF()
        return validader.validate(docum)
    
    def maca(self):
        masca = CPF()
        return masca.mask(self.cpf)

class doccnPj:
    def __init__(self, docum):
        if self.valida(docum):
            self.cnpj = docum
        else:
            raise ValueError ("é nois na fita ")

    def valida(self, docum):
        validader = CNPJ()
        return validader.validate(docum)
    
    def masca(self):
        masca = CNPJ()
        return masca.mask(self.cnpj)
    
é = "77890342004"
S = DCocumento.cria_doc(é)
print(S)