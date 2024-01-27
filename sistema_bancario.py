import datetime as dt
from time import sleep
from os import system
# import json
nr_conta = 1
# DIR = 'Bank.json'
# def read_json(dir, object):
#     dados = []
#     try:
#         with open(dir, 'r', encoding='utg-8') as items:
#             dados = json.load(items) 
#     except:
#         with open(dir, 'a', encoding='utf-8') as items:
#             dados = json.dump(object, items, indent=2, ensure_ascii=False)
#     return dados

# def save_json(dir, object):
#     with open(dir, 'a', encoding='utf-8') as items:
#             dados = json.dump(object, items, indent=2, ensure_ascii=False)
#     return dados

def menu():
    opcao = input(f'''********Escolha uma opção********
\t1 - Fazer Saque
\t2 - Fazer Deposito
\t3 - Ver Extrato
\t4 - Criar Conta
\t5 - Criar Usuário
\t6 - Ver Contas
\t7 - Ver Usuários
\t0 - Sair
*********************************
''')
    try:
        opcao = int(opcao)
    except ValueError:
        print('Digite somente numeros!')
        sleep(2)
        system('cls')
        return 99
    return opcao

def depositar(valor, extrato, saldo, /):
    try:
        deposito = float(valor)
    except:
        system('cls')
        print('\ndigite um valor numerico')
        sleep(2)
        system('cls')
        return
    saldo += deposito
    system('cls')
    print(f'\nSeu saldo atual é: R${saldo:.2f}')
    extrato = (f'{dt.datetime.today().now().strftime("%d/%m/%Y %H:%M:%S")} foi feito o depoisito de R${deposito:.2f} ficando um total R${saldo:.2f}')
    sleep(2)
    system('cls')
    return saldo, extrato

def sacar(*, saques, limite, LIMITE_SAQUE, valor, extrato, saldo):
    # global saldo, extrato, saques, LIMITE_SAQUE, limite
    saque = 0
    if saques > LIMITE_SAQUE:
        system('cls')
        print(f'\nSeu limite diario de saque foi alcançado\n')
        sleep(2)
        system('cls')
        return extrato, saldo, saques
    try:
        saque = float(valor)
    except:
        system('cls')
        print(f'\ndigite um valor numerico') 
        sleep(2)
        system('cls')
        return extrato, saldo, saques
    if saldo < saque:
        system('cls')
        print(f'\nSaldo insuficiente, você tem: {saldo:.2f}')
        sleep(2)
        system('cls')
        return extrato, saldo, saques 
    
    elif limite < saques:
        system('cls')
        print(f'\nQuantidade muito alta, limite é {limite:.2f}')
        sleep(2)
        system('cls')
        return extrato, saldo, saques
    
    else: 
        saldo -= saque
        extrato = (f'{dt.datetime.today().now().strftime("%d/%m/%Y %H:%M:%S")} foi feito o saque de {saque:.2f} ficando um total de {saldo:.2f}')
        system('cls')
        print(f'Seu saldo atual é: {saldo:.2f}')

    saques += 1
    sleep(2)
    system('cls')
    return extrato, saldo, saques
    
def ver_extrato(extrato):
    system('cls')
    print('*****************Seu extrato***************** ')
    if not extrato:
        system('cls')
        print('''******************************************
       Você não teve movimentação!!
******************************************''')
        sleep(2)
        system('cls')
        return
    print()
    for _ in extrato:
        print(f'{_}')
        print('-'*len(_))
    sleep(5)
    system('cls')

def criar_conta(cpf, contas, agencia):
    global nr_conta
    valida = []
    if len(cpf) < 11:
        print('Obrigatório digitar os 11 digitos do CPF')
        sleep(2)
        system('cls')
        return contas
    try:
        cpf = int(cpf)
    except ValueError:
        print('Somente numeros são validos no CPF!')
        sleep(2)
        system('cls')
        return contas
    for _ in contas:
        valida.append(int(_['CPF'].replace('.','').replace('-','')))
    if cpf in valida:
        cpf = str(cpf)
        system('cls')
        print('CPF já cadastrado')
        conta = [{'Agencia': agencia,
                  'Conta': nr_conta,
                  'Nome Cliente': _['Nome Cliente'],
                  'CPF': '{}.{}.{}-{}'.format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:]),}]
        sleep(2)
        system('cls')
        nr_conta += 1
        return conta
    cpf = str(cpf)
    print('CPF não localizado!')
    conta = [{'Agencia': agencia,
              'Conta': nr_conta,
              'Nome Cliente': input('Digite seu nome: '),
              'CPF': '{}.{}.{}-{}'.format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:]),}]
    sleep(2)
    system('cls')
    nr_conta += 1
    return conta

def criar_usuario(cpf, usuarios):
    valida = []
    if len(cpf) < 11:
        print('Obrigatório digitar os 11 digitos do CPF')
        sleep(2)
        system('cls')
        return usuarios
    try:
        cpf = int(cpf)
    except ValueError:
        print('Somente numeros são validos no CPF!')
        sleep(2)
        system('cls')
        return usuarios
    for _ in usuarios:
        valida.append(int(_['CPF'].replace('.','').replace('-','')))
    if cpf in valida:
        system('cls')
        print('CPF já cadastrado')
        sleep(2)
        system('cls')
        return
    system('cls')
    cpf = str(cpf)
    print('CPF não localizado!')
    __name = input('Digite seu nome: ')
    __dt_nasc = input('Digite a data do seu nascimento: ')
    if len(__dt_nasc) != 8:
        if not isinstance(__dt_nasc, int):
            system('cls')
            print('Digite somente numeros da data')
            sleep(2)
            system('cls')
            return usuarios
    __logradouro = input('digite o seu logradouro: ')
    __nro = input('Digite o numero: ')
    __bairro = input('Digite o bairro: ')
    __cidade = input('Digite a cidade: ')
    __estado = input('Digite a sigla do estado: ')
    usuario = [{'Nome': __name,
                'CPF': '{}.{}.{}-{}'.format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:]),
                'Data nascimento': '{}/{}/{}'.format(__dt_nasc[:2], __dt_nasc[2:4], __dt_nasc[4:]),
                'Endereço': '{}, {} - {} - {}/{}'.format(__logradouro, __nro, __bairro, __cidade, __estado),}]
    sleep(2)
    system('cls')
    return usuario
    
def listar_contas(contas):
    system('cls')
    print('*****************Lista de Contas***************** ')
    if not contas:
        system('cls')
        print('''******************************************
       Sem contas cadastradas!!
******************************************''')
        sleep(2)
        system('cls')
        return
    for _ in contas:
        print(f'{_}')
    sleep(5)
    system('cls')

def listar_usuarios(usuarios):
    system('cls')
    print('*****************Lista de Usuários***************** ')
    if not usuarios:
        system('cls')
        print('''******************************************
       Sem contas cadastradas!!
******************************************''')
        sleep(2)
        system('cls')
        return
    for _ in usuarios:
        print(f'{_}')
    sleep(5)
    system('cls')

def main():
    __AGENCIA = '0001'
    __LIMITE_SAQUE = 3
    __LIMITE = 500
    saldo = 0
    _extrato = []
    extrato = ''
    _usuarios = []
    _contas = []
    saques = 1

    while True:
        opcao = menu()
        validos = [1,2,3,4,5,6,7,0]

        if opcao == 0:
            break
        elif opcao not in validos:
            system('cls')
            print(f'\nDigite uma opção valida!!\n')
            sleep(2)
            system('cls')
        elif opcao == 1:
            (extrato, saldo ,saques) = (sacar(saques=saques, limite = __LIMITE, LIMITE_SAQUE=__LIMITE_SAQUE, valor=input('Digite a quantidade para sacar: '), extrato=extrato, saldo=saldo))
            if not extrato:
                continue
            _extrato.append(extrato)
        elif opcao == 2:
            (saldo, extrato) = (depositar(input('Digite a quantidade para depositar: '), extrato, saldo))
            _extrato.append(extrato)
        elif opcao == 3:
            ver_extrato(_extrato)
        elif opcao == 4:
            _contas.extend(criar_conta(input('Digite o CPF: '), _contas, __AGENCIA))
        elif opcao == 5:
            try:
                _usuarios.extend(criar_usuario(input('Digite o CPF: '), _usuarios))
            except TypeError:
                continue
        elif opcao == 6:
            listar_contas(_contas)
        elif opcao == 7:
            listar_usuarios(_usuarios)
main()
