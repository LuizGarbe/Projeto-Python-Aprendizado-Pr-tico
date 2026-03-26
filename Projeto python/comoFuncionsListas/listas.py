# Adiciona o valor naposição que deseja. nesse caso valor 100 na posição 3 da lista 
# idade[10,20,40]
# idade.insert(3,100)

# Adiciona o valor no final da lista 
# idade.append(8)

# Deleta o que você escolher 
# idade.remove(100)

# Procura a oque você quer 
# imprime = idade.index(60)
# print(imprime)

# Usando lista comprehension sendo a parte de output que seria =[proximo_ano(idade)], collection que seria = [for idade in idades], condition que seria = [if idade >= 45]
#def proximo_ano(idade):
    #return idade += 1
#resultado = [proximo_ano(idade) for idade in idades if idade >= 45]
#print(resultado)
#basicamente a mesma coisa
#idades_ano_que_vem = [idade+1 for idade in idades] # è a mesma coisa da questão de cima, mas simplificado
#print(idades_ano_que_vem)

#Listas são mutaveis e isso que esta embaixo seria uma solução para rebeber um valor 0, sendo assim não fique atribuindo valores novos todas as vezes que for solicitada
#def visualização(lista = None):
    #if lista == None:
        #lista = list ()
    #print(len(lista))
    #print(lista)
    #lista.append(13) # vai adicionar o valor 13 na lista.

#visualização()

# explicação sobre tuplas
#class ContaCorrente:
    #def __init__(self, codigo):
        #self.codigo = codigo
        #self.saldo = 0

    #def deposita(self,valor):
        #self.saldo += valor

    #def __str__(self):
        #return "[Codigo {} Saldo {}]".format(self.codigo, self.saldo)
    
    #conta_do_lu = ContaCorrente(15)
    #conta_do_lu.deposita(600)
    #print(conta_do_lu)

    #conta_do_gui.deposita(500)
    #print(conta_do_lu)

    #conta_dani = ContaCorrente(47)
    #conta_dani.deposita(600)
    #print(conta_dani)

    #contas = [conta_dani, conta_do_lu, conta_do_lu] #pode repetir um valor e assim ela passar o mesmo valor para os dois atributos por serem mutaveis
    #print(contas)

    #for conta in contas:
        #print(contas)

    #print(contas[1])

    #def deposita_contas (contas):
       #for conta in contas:
        #conta.deposita(100)
    
    #print(contas[0], conta[1])
    #deposita_contas(contas)
    #print(contas[0], contas[1])

    #contas.insert(0, 76) #atribuir um avalor
    #print(contas[0], contas[1], contas[2]) #vai dar errado pois ele vai intender que não é possivel atribuir um avalor na posição 0

    #para resolver isso usa uma tupla, pois ela não é mutavel, mas ela tem que possuir um organização que é feita por você

    #conta_do_gui = ("Gui", 15, 1935)
    #conta_do_gui[1]
    #conta_do_gui[1] += 100 

    #def deposita_idade(conta): # é uma forma eficiente de depositar acrecentar um valor em um tupla
        #novo_saldo = conta[1]+ 100
        #codigo = conta [2]
        #return (codigo, novo_saldo)
    
    #usuarios = ["guilherme", "luiz"] # é possivel colocar uma lista em uma tupla para atribuir novos parametos na lista 
    # pode alterar o valor da tupla expecificando, por exemplo o código escrito abaixo
    #contas[1].deposita(300)

    # Polimorfismo 
#from abc import ABCMeta, abstractmethod
#class Conta:
    #def __init__(self, codigo):
        #self._codigo = codigo
        #self._saldo = 0

    #def deposita(self,valor):
        #self._saldo += valor

    #@abstractmethod
    #def passa_o_mes(self):
        #pass

    #def __str__(self):
        #return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    
#class ContaCorrente (Conta):
    #def passa_o_mes(self):
        #self._saldo -= 2

#class ContaPoupanca (Conta):
    #def passa_o_mes(self):
        #self._saldo *= 1.01
        #self._saldo -= 3

#class ContaInvestimento(Conta):
    #pass

#ContaInvestimento(98)

#conta16 = ContaCorrente(16)
#conta16.deposita(1000)
#conta16.passa_o_mes()

#conta56 = ContaPoupanca(56)
#conta56.deposita(2000)
#conta56.passa_o_mes()

#contas = [conta16, conta56]

#saldo_antes = [str(conta) for conta in contas]
#for conta in contas:
    #conta.passa_o_mes()

#saldo_depois = [str(conta) for conta in contas]
#for antes, depois in zip(saldo_antes, saldo_depois):
    #print(antes)
    #print(depois)

# Como funciona __eq__
#class Conta:
    #def __init__(self, codigo):
        #self._codigo = codigo
        #self._saldo = 0

    #def __eq__(self, outro):
        #if type(outro) != ContaSalario:
            #return False
        #return self._codigo == outro._codigo and self._saldo == self._saldo

    #def deposita (self, valor):
        #self._saldo += valor

    #def __str__(self):
        #return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    
#class ContaSalario(Conta):
    #pass

#class ContaCorrente(Conta):
    #pass

#class MultiploSalario(ContaSalario):
    #pass

#conta1 = ContaSalario(16)
#conta2 = ContaCorrente(16)

#print(conta1 == conta2)

#isinstance(ContaCorrente(16), ContaCorrente)    
#isinstance(ContaCorrente(16), Conta)

# Como funciona outro builtins
#idades = [10, 20, 90, 69, 38, 46, 92]
#for indice , idades in enumerate(idades):
    #print(indice, "X", idades)

#print("__________________________________________\n")

#usuarios = [
    #("Guilherme", 29, 1934),
    #("Rafael", 23, 1931),
    #("Cleber", 30, 1935)
#]

#for name, idade, ano in usuarios:
    #print(name)

#É a mesma coisa que o de cima
#modelos = ["Mercedes amg gt bs", "Ferrari 488 pista", "Porsche gt2 rs", "Lamborghini murcielago sv", "Ferrari purosangue", "Mclaren speedtail"]

#for indice, modelos in enumerate(modelos):
    #print(indice, "=", modelos)

#print("______________________________\n")

#descrição = [
    #("Mercedes amg gt bs", 2017, "v8-Biturbo"),
    #("Ferrari 488 pista", 2017, "V8-Turbo"),
    #("Porsche gt2 rs", 2017, "boxter 3.6-Biturbo"),
    #("Lamborghini murcielago sv", 2009, "V12-Aspirado"),
    #("Ferrari purosangue", 2024, "V12-Aspirado" ),
    #("Mclaren speedtail",2020, "v8-biturbo e um motor eletrico")
#]

#for nome, ano, motor in descrição:
    #print(nome, ano)

#Como funciona Ordem natural
#idades = [10, 20, 90, 69, 38, 46, 92]
#print(sorted(idades)) #(imprime o valor idade em seguéncia crescente)
#print(sorted(idades, reverse=True))

#nomes = ["Mercedes amg gt bs", "Ferrari 488 pista", "Porsche gt2 rs"]
#print(sorted(nomes))

#class Conta:
    #def __init__(self, codigo):
        #self._codigo = codigo
        #self._saldo = 0

    #def __eq__(self, outro):
        #if type(outro) != ContaSalario:
            #return False
        #return self._codigo == outro._codigo and self._saldo == self._saldo

    #def __lt__(self, outro):
        #return self._saldo < outro._saldo
    
    #def deposita (self, valor):
        #self._saldo += valor

    #def __str__(self):
        #return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    
#class ContaSalario(Conta):
    #pass

#class ContaCorrente(Conta):
    #pass

#class MultiploSalario(ContaSalario):
    #pass

#conta_gui = ContaSalario(17)
#conta_gui.deposita(100)

#conta_paulo = ContaSalario(23)
#conta_paulo.deposita(200)

#conta_lu = ContaSalario(34)
#conta_lu.deposita(600)

#print(conta_gui < conta_lu)

#contas = [conta_lu, conta_gui, conta_paulo]

#for conta in sorted(contas, reverse= True):
    #print(conta)

#from operator import attrgetter (funcion apenas importando o attrgetter)
#for conta in sorted(contas, key=attrgetter("_saldo")): # Vai pegar a chave do atribudo que foi instanciado
    #print(conta)

#from functools import total_ordering # da a opção de colocar <= como forma de comparação, exemplo: (conta_gui <= conta_lu) retorna= False

#@total_ordering
#class Conta:
    #def __init__(self, codigo):
        #self._codigo = codigo
        #self._saldo = 0

    #def __eq__(self, outro):
        #if type(outro) != ContaSalario:
            #return False
        #return self._codigo == outro._codigo and self._saldo == self._saldo

    #def __lt__(self, outro):
        #if self._saldo != outro._saldo:
            #return self._saldo < outro._saldo
        #else:
            #return self._codigo < outro._codigo
    
    #def deposita (self, valor):
        #self._saldo += valor

    #def __str__(self):
        #return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)

#@total_ordering
#class ContaSalario(Conta):
    #pass

#@total_ordering
#class ContaCorrente(Conta):
    #pass

#@total_ordering
#class MultiploSalario(ContaSalario):
    #pass

#conta_gui = ContaSalario(17)
#conta_gui.deposita(1000)

#conta_paulo = ContaSalario(23)
#conta_paulo.deposita(200)

#conta_lu = ContaSalario(14)
#conta_lu.deposita(100)

#print(conta_gui < conta_lu)

#contas = [conta_lu, conta_gui, conta_paulo]

#for conta in sorted(contas, reverse= True):
    #print(conta)

#print(conta_gui <= conta_lu)
#print(conta_lu <= conta_paulo)
#print(conta_paulo <= conta_gui)

#Continuação 
#tipo_de_motores = {3, 4, 5, 6,}
#mais_usados = {3, 4, 8, 10}

#resultado_da_pesquisa = tipo_de_motores.copy()
#resultado_da_pesquisa.update(mais_usados)
#set(resultado_da_pesquisa) # vai motrar a lista sem repetir os valores
#print(set(resultado_da_pesquisa))

#poded usar os dois tipos o de cima e o de baixo

#ou = tipo_de_motores | mais_usados
#print(ou)

#mesmo_conjunto = tipo_de_motores & mais_usados
#print(mesmo_conjunto)

#remove_itens_repetidos = tipo_de_motores - mais_usados
#print(remove_itens_repetidos)

#ou_exclusivo = tipo_de_motores ^ mais_usados
#print(ou_exclusivo) #fez isso ou aquilo, não as duas coisas 

#Continuação da funcionalidade de dicionario
#numeros = {10,20,30,40,50,60,70,80}
#numeros.add(100)
#frozenset(numeros)
#print(numeros)

#texto = "Eu vou ter uma amg gt black series"
#set(texto.split()) # Ja o split tira os espaços embrencos
#print(set(texto.split())) # o set tira as palavras reptidas

#carros = {
    #"Amg gt bs": 1,
    #"Gt2 rs":2, 
    #"Rocket 900": 3
#}
#carros["G 63 amg"] = 4 # adiciona 
#del carros["G 63 amg"] # deleta
#verifica_sepossui_o_elemento = carros.get("Gt2 rs", 0)
#print(verifica_sepossui_o_elemento)

#for elemeto in carros: # pode usar (keys) que passa pelas chaves, (values) que passa pelos valores , (items) que passa de intem por item
    #valores = carros[elemeto] # Nesse caso ele passa tudo que estiver no dicionario, linha por linha
    #print(elemeto, "=", valores)

#mais_carro = ["carro = {}".format(chave) for chave in carros.keys()]
#print(mais_carro)

#continuação
#texto = "Eu vou ter uma amg gt black series"
#texto = texto.lower() #Deixa o texto em minusculo

#from collections import defaultdict. Nessa parte eu possivel usar duas formas para contar o numero de palavras com valor padrão (defaultdict) e (counter)
#carros = {
    #"Amg gt bs": 1,
    #"Gt2 rs": 2, 
    #"Rocket 900": 3
#}

#carros = defaultdict(int)

#for palavra in texto.split():
    #ate_agora = carros[palavra, 0]
    #carros[palavra] += 1

#texto = "Eu vou ter uma amg gt black series"
#texto = texto.lower() #Deixa o texto em minusculo

#from collections import Counter
#carros = {
    #"Amg gt bs": 1,
    #"Gt2 rs": 2, 
    #"Rocket 900": 3
#}
#carros = Counter(texto.split())
#print(carros)

from collections import Counter
texto1 = """
Enquanto esperamos ansiosos para que a Mercedes-AMG revele o híbrido GT73 com uma potência estimada de 800 cv, a Brabus preparou algo ainda mais intenso. Conheça o Rocket 900, que embora não tenha sob o capô o motor V12 como os modelos “Rocket” anteriores do preparador alemão, ainda sim chama a atenção pelos dados da ficha técnica. A joia do construtor sediado em Bottrop começou a vida como um GT63 S antes de receber o tratamento facial e muscular.

A atualização mais importante sobre o modelo padrão está embaixo do capô, onde o motor V8 biturbo foi fortemente modificado para aumentar o deslocamento de 4,0 para 4,5 litros. A Brabus também instalou um par de turbocompressores maiores e uma pressão de alimentação máxima mais alta. A potência adicionada exigiu sistema de arrefecimento extra, então foram instaladas entradas de ar do tipo ram confeccionadas em carbono à esquerda e à direita da grade do radiador.

O resultado final é uma potência impressionante de 900 cv e gigantescos 127 m.kgf de torque. No entanto, a Brabus instala um limitador eletrônico para proteger o trem de força limitando o torque a “apenas” 107 m.kgf. Fazendo as contas, a potência em comparação com uma série GT63 S foi superada por incríveis 258 cv e 15,3 m.kgf de torque.

Você pode imaginar que o aumento significativo de potência teve um grande impacto no desempenho. O GT63 S regular já está entre os carros de quatro portas mais rápidos, mas o Brabus Rocket 900 leva as coisas a um nível totalmente novo. Ele faz 0 a 100 km/h em 2,8 segundos, 0 a 200 km/h em 9,7 e 0 a 300 km/h em 23,9 segundos. A Brabus diz que teve que limitar a velocidade máxima em 330 km/h devido ao alto peso do carro e para proteger os pneus.

Outras modificações incluem também um sistema de escape quádruplo de aço inoxidável - o afinador alemão respeitável também trabalhou no design do carro, desenvolvendo um kit de carroceria agressivo com detalhes em fibra de carbono. O novo kit de carroceria alarga a traseira do GT em mais 7,8 cm quando comparado ao similar original. Vale ressaltar que todas as peças do kit de carroceria foram otimizadas no túnel de vento para maior eficiência aerodinâmica.

O Rocket 900 está equipado com rodas forjadas pelas próprias Brabus com diâmetros de 21 pol na dianteira e 22 pol, com discos aerodinâmicos de carbono exposto. Ele está cerca de 2,5 cm mais baixo graças a uma suspensão pneumática desenvolvida pela Brabus com os modos Comfort e Sport selecionáveis.

A Brabus está irá converter apenas 10 “cupês” Mercedes-AMG GT63 S para a especificação Rocket 900 e cada carro virá com uma variedade de ajustes dentro da cabine. Apresentando uma pintura Stealth Grey, o primeiro do grupo tem couro preto e Alcântara no interior, onde também há costura decorativa cinza e nada menos que 215 peças pintadas com uma cor correspondente ao da carroceria. Completam a lista de atualizações as chapas de aço inoxidável, elementos de carbono com acabamento brilhante e até tapetes sob medida.
"""
texto2 = """
The Mercedes-Benz 190E, introduced in the early 1980s, holds a significant place in the history of luxury compact sedans. Launched as part of the W201 series, the 190E was designed to combine the elegance and engineering prowess synonymous with the Mercedes-Benz brand in a more compact form.

Debuting at the Geneva Motor Show in 1982, the 190E showcased Mercedes-Benz's commitment to quality craftsmanship and advanced technology. The "E" in its name stood for "Einspritzung," indicating fuel injection in German, highlighting the model's modern and efficient engine technology.

One of the standout features of the 190E was its innovative suspension system. Mercedes-Benz engineers employed a sophisticated multi-link rear suspension, contributing to the car's exceptional handling and ride comfort. This technology trickled down from the brand's higher-end models, emphasizing Mercedes-Benz's dedication to incorporating cutting-edge advancements across its lineup.

Under the hood, the 190E housed a range of engines, including four-cylinder and six-cylinder options, providing a balance between performance and fuel efficiency. The 190E's timeless design, characterized by its clean lines and signature grille, echoed the brand's luxury aesthetic while maintaining a distinct identity within the compact segment.

Motorsport enthusiasts fondly remember the 190E due to its involvement in touring car racing. The model became the basis for the renowned Mercedes-Benz 190E 2.3-16, developed in collaboration with Cosworth. This high-performance variant featured a powerful 16-valve engine and aerodynamic enhancements, dominating the racetracks and solidifying the 190E's reputation for both luxury and performance.

The Mercedes-Benz 190E remained in production until the mid-1990s, leaving a lasting legacy as a well-engineered and stylish compact luxury sedan. Its influence can be seen in subsequent Mercedes-Benz models, as the brand continues to evolve and set new standards in the automotive industry.
"""

def analisa_frequencia(texto1):
    aparicoes = Counter(texto1.lower())
    total_caracteres = sum(aparicoes.values())
    porcentagem = [(letra, frequencia / total_caracteres)for letra, frequencia in aparicoes.items()]  # Nesse caso vai mostrar a porcentagem de aprarições das letra, que é letra e frequencia dividido pelo total de caracteres ´pr 
    porcentagem = Counter(dict(porcentagem))
    mais_comuns = porcentagem.most_common(10)

    for carcteres, proporção in mais_comuns:
        print("{} -> {:.2f}%".format(carcteres, proporção * 100)) #O numero doisnessa função:({:.2f}%"). tem como função mostra o dosi numros decimais depois do ponto emxemplo:  16.87%

analisa_frequencia(texto1)
print("______________________")
analisa_frequencia(texto2)