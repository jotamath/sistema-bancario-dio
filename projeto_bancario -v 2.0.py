# Projeto Bancário


def menu():
    MENU = """
    [d] Depositar
    [s] Saque
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [a] Sair

    ==> """
    return input(MENU)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato = f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Não foi possível fazer a operação.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQ):
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
        print("Saque realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato


def Extrato(saldo, extrato):
    print("\n-------EXTRATO-------")
    print("Não realizou operações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("--------------------")
    return saldo, extrato


def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    # se usuario --> ja existe conta com esse cpf
    if usuario:
        print("Já existe usuário com esse CPF")
        return

    nome = input("Informe seu nome completo: ")
    data_nasc = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Digite seu endereço (logradouro, nr - bairro, cidade/UF): ")

    # adiciona esse usuario ao banco de dados (append)
    usuarios.append({"nome": nome, "data_nasc": data_nasc,
                    "cpf": cpf, "endereco": endereco})
    # printa aviso
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta,
                "usuario": usuario}
    print("Usuário não encontrado, tente a opção de novo usuário.")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta["agencia"]}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("="*50)
        print(linha)


def Main():

    saldo = 0
    limite = 500
    AGENCIA = "0001"
    extrato = ''
    numero_saques = 0
    LIMITE_SAQ = 3
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        selecao_menu = menu()
    # Operação de Depósito
    # variavel deposito
        if selecao_menu == "d":
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
    # Operação de Saque
        elif selecao_menu == "s":
            valor = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQ=LIMITE_SAQ
            )
    # Operação de Extrato
        elif selecao_menu == "e":
            Extrato(saldo, extrato=extrato)
    # Criar novo usuario
        elif selecao_menu == "nu":
            novo_usuario(usuarios)
    # Criar nova conta
        elif selecao_menu == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
    # Listar contas
        elif selecao_menu == "lc":
            listar_contas(contas)
    # Sair
        elif selecao_menu == "a":
            break
    # Caso de erro geral
        else:
            print("Operação inválida.")


Main()
