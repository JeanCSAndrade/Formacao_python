# main.py
import textwrap
from os import system
from time import sleep
from cliente import PessoaFisica
from conta import ContaCorrente
from transacao import Deposito, Saque

def menu():
    menu = """\n
    ================ MENU ================
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Nova conta
    5 - Listar contas
    6 - Novo usuário
    0 - Sair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n#### Cliente não encontrado! ####")
        return

    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n#### Cliente não encontrado! ####")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n#### Cliente não encontrado! ####")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        system('cls')
        print("\n#### Cliente não encontrado! ####")
        sleep(1)
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    system('cls')
    print("\n*****************SEU EXTRATO*****************")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = '''******************************************
       Você não teve movimentação!!
******************************************'''
    else:

        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: R$ {transacao['valor']:.2f}\n{transacao['data']}"
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")
    sleep(3)
    system('cls')
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n#### Cliente já registrado na base de dados! ####")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    __logradouro = input('digite o seu logradouro: ')
    __nro = input('Digite o numero: ')
    __bairro = input('Digite o bairro: ')
    __cidade = input('Digite a cidade: ')
    __estado = input('Digite a sigla do estado: ')
    endereco = '{}, {} - {} - {}/{}'.format(__logradouro, __nro, __bairro, __cidade, __estado)

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n######### CPF não encontrado na base de clientes #########")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))

def main():
    clientes = []
    contas = []

    while True:
        try:
            opcao = int(menu())
        except TypeError:
            print('Digite apenas o numero da opção!!')
            continue

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_cliente(clientes)

        elif opcao == 0:
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

main()