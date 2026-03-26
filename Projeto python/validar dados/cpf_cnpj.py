from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCPF(doc_str)
        elif len(doc_str) == 14:
            return DocCNPJ(doc_str)
        else:
            raise ValueError("Esse documento não existe ou é inválido")

class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Esse CPF não existe ou é inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Esse CNPJ não existe ou é inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

doc = "67599782001"
v_n = Documento.criar_novo(doc)
print(v_n)