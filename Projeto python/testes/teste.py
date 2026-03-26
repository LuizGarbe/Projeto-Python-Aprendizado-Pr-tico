def conta1f  (numero, titular,saldo,limite):
    conta = {"numero_conta": numero, "titular_conta": titular, "saldo_conta": saldo, "limite_conta": limite}
    return conta

def depositar(conta,valor):
    conta["saldo"] += valor

def sacar(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("sua conta possui R${}".format(conta["saldo"]))