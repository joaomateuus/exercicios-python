from datetime import date
menu = ""

"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
valor_diario = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("Digite a operação que deseja realizar: s-saque, d-deposito, e-extrato, q-sair")
    opcao = input(menu)
    
    if opcao == "d":
        print("Digite quanto deseja depositar em sua conta: ")
        valor_deposito = float(input())
        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato_deposito = {
                "Dia da transação": date.today(),
                "Valor do deposito": valor_deposito,
                "saldo_atual": saldo
            }
            extrato.append(extrato_deposito)
            print(f"Operação realizada com sucesso, SALDO ATUAL {saldo}")    
        else:
            print("Operação não realizada, valor do deposito invalido")       
    
    elif opcao == "s":
        print(f'Voce tem {saldo} na sua conta')
        print(f"Seu limite diario para saque é: R${valor_diario}")
        print(f'Voce possui {numero_saques} saques realizados')
        print("Digite quanto deseja sacar:")
        
        valor_saque = float(input())
        if(numero_saques >= LIMITE_SAQUES):
            print(f"Operação invalida limite saques diarios excedidos")
        elif(valor_saque > float(valor_diario)):
            print(f"Esse valor ultrapassa seu limite diario de saques")
        elif(valor_saque > float(saldo)):
            print(f"Voce não tem saldo suficiente para efetuar essa transação, SALDO ATUAL: {saldo}")
        elif valor_saque > 0:
            numero_saques += 1
            valor_diario -= valor_saque
            saldo -= valor_saque
            extrato_saque = {
                "Dia da transação": date.today(),
                "Valor do Saque": valor_saque,
                "saldo_atual": saldo
            }
            extrato.append(extrato_saque)
            print(f"Operação feita com sucesso, SAQUE REALIZADO: {valor_saque} SALDO ATUAL: R${saldo}")
        else:
            print("Operação falhou valor inválido")  
    
    elif opcao == "e":
        if(len(extrato) > 0):
            print("Segue historico de transações de sua conta bancaria: ")
            print(extrato)
        else:
            print(f"Voce não possui nenhuma transação realizada, e seu saldo atual é de: R${saldo}")
            break
    elif opcao == "q":
        break
    else:
        print("Operacao invalida, eschola uma opção")