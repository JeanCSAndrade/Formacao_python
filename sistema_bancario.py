import datetime as dt
from time import sleep
from os import system
saldo = 0
limite = 500
extrato = []
saques = 0
LIMITE_SAQUE = 3

def Deposito(qtd):
    global saldo, extrato
    try:
        deposito = float(qtd)
    except:
        system('cls')
        print('\ndigite um valor numerico')
        sleep(2)
        system('cls')
        return
    saldo += deposito
    system('cls')
    print(f'\nSeu saldo atual é: R${saldo:.2f}')
    extrato.append(f'{dt.datetime.today().now().strftime("%d/%m/%Y %H:%M:%S")} foi feito o depoisito de R${deposito:.2f} ficando um total R${saldo:.2f}')
    sleep(2)
    system('cls')

def Sacar(qtd):
    global saldo, extrato, saques, LIMITE_SAQUE, limite
    saques += 1
    if saques > LIMITE_SAQUE:
        system('cls')
        print(f'\nSeu limite diario de saque foi alcançado\n')
        sleep(2)
        system('cls')
        return
    try:
        saque = float(qtd)
    except:
        saques - 1
        system('cls')
        print(f'\ndigite um valor numerico') 
        sleep(2)
        system('cls')
    if saldo < saque:
        saques - 1
        system('cls')
        print(f'\nSaldo insuficiente, você tem: {saldo:.2f}')
        sleep(2)
        system('cls')
        return
    
    elif limite < saque:
        saques - 1
        system('cls')
        print(f'\nQuantidade muito alta, limite é {limite:.2f}')
        sleep(2)
        system('cls')
        return
    else: 
        saldo -= saque
        extrato.append(f'{dt.datetime.today().now().strftime("%d/%m/%Y %H:%M:%S")} foi feito o saque de {saque:.2f} ficando um total de {saldo:.2f}')
        system('cls')
        print(f'Seu saldo atual é: {saldo:.2f}')
    sleep(2)
    system('cls')
    

def Extrato():
    global extrato
    system('cls')
    print('Seu extrato é: ')
    if not extrato:
        system('cls')
        print('''###########################################
       Você não teve movimentação!!
###########################################''')
        sleep(2)
        system('cls')
        return
    for _ in extrato:
        print(f'\n{_}')
    sleep(2)
    system('cls')

operacao = {
    'd': lambda: Deposito(input('Digite a quantidade para depositar: ')),
    's': lambda: Sacar(input('Digite a quantidade para sacar: ')),
    'e': lambda: Extrato()
}
while True:
    validos = ['q','s','e','d']
    opcao = input(f'''Escolha uma opção:
\t"s" para Sacar
\t"d" para Depositar
\t"e" para ver o extrato
\t"q" para sair
''')
    if opcao == 'q':
        break
    elif opcao not in validos:
        system('cls')
        print(f'\nDigite uma opção valida!!\n')
        sleep(2)
        system('cls')
    else: 
        comando = operacao.get(opcao)
        comando()