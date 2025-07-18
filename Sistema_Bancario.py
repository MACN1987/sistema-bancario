import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

Menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair



"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    limpar_tela()
    print("Bem-vindo ao Sistema Bancário!")
    print("Selecione uma opção:")
    opcao = input(Menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'O Depósito de R$ {valor:.2f} foi realizado com sucesso!, Tenha um ótimo dia!')
        else:
            print("O Valor informado é invalido, tente novamente, por favor!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque que deseja realizar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("O valor para saque é maior que o saldo disponível! Por favor, consulte o seu extrato.")
        
        elif excedeu_limite:
            print(f"O valor para saque não pode ser maior que R$ {limite:.2f}, por favor, tente novamente")
        
        elif excedeu_saques:
            print(f"Voce já atingiu o limite diário de saques, que é de {limite_saques} saques. "
                  "Por favor, tente novamente amanhã ou entre em contato com seu gerente")

        elif valor > 0:
            saldo -= valor
            extrato += f"Foi realizado um saque de R$ {valor:.2f}\n"
            numero_saques += 1
            print (f"O saque de R$ {valor:.2f} foi realizado com sucesso!, tenha um ótimo dia!")
        else:
            print("O valor informado é inválido, por favor, tente novamente!")

    elif opcao == "3":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário, tenha um ótimo dia!")
        input("\nPressione Enter para sair...")
        limpar_tela()
        continue
    else:
        print("Opção inválida, por favor, tente novamente!")

    input("\nPressione Enter para continuar...")
    
    
    
    





