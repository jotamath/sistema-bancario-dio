# Projeto Bancário
menu = """
[d] Depositar
[s] Saque
[e] Extrato
[a] Sair

==> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQ = 3

while True:
    selecao_menu = input(menu)
# Operação de Depósito
# variavel deposito
    if selecao_menu == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Não foi possível fazer a operação.")

# Operação de Saque
# 3 saques diarios, limite máx == 500,
# if usuario sem saldo => saque impossível
# saques armazenados em uma variavel e exibidos na op extrato
    if selecao_menu == "s":
        valor = float(input("Digite o valor do saque: "))

        if valor > limite:
            print("O valor do saque supera o limite.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif numero_saques > LIMITE_SAQ:
            print("Limite de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato = f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido.")

# Operação de Extrato
# listar todos os depósitos e saques realizados na conta
# no formato R$ XXXX.XX
    if selecao_menu == "e":
        print("\n-------EXTRATO-------")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------")
    elif selecao_menu == "a":
        break

    else:
        print("Operação inválida.")
