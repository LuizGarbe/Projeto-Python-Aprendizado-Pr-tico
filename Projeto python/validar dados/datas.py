from datetime import datetime, timedelta

class Datas_ptbr:
    def __init__(self):
        self.momentoCadastro = datetime.today()
    
    def __str__(self):
        return self.formataData()
    
    def mesDoOcorrido (self):
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes = self.momentoCadastro.month - 1 
        return meses[mes] 
    
    def diaSemanaDoOcorrido (self):
        semana = [
            "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Fereira", "Sabado", "Domingo"
        ]
        diaSemana= self.momentoCadastro.weekday
        return semana[diaSemana]
    
    def formataData (self):
        dataFormatada = self. momentoCadastro.strftime("%d/%m/%Y  %H:%M")
        return dataFormatada

    def tempoCadastro (self):
        tempoDeCadastro = (datetime.today() + timedelta(days=30,hours=720, minutes=25, seconds=47)) - self.momentoCadastro
        return tempoDeCadastro
    
# Criar uma instância da classe
data_ptbr = Datas_ptbr()

# Imprimir a data formatada
print(data_ptbr.tempoCadastro())
