import datetime as dt
from time import sleep
from os import system
from abc import ABC, abstractmethod, abstractclassmethod

class Client:
    def register_client(self, address):
        self.address = address
        self.__account = []

    
    def action_register(self, action=0):
        while True:
            try:
                action = int(input(f'''********Escolha uma opção********
\t1 - Fazer Saque
\t2 - Fazer Deposito
\t3 - Ver Extrato
\t4 - Criar Conta
\t5 - Criar Usuário
\t6 - Ver Contas
\t7 - Ver Usuários
\t0 - Sair
*********************************
'''))
            except ValueError:
                print('Digite somente numeros!')
                sleep(2)
                system('cls')
                continue
            Action.register(action)
            return
    
    def create_account(self, conta):
        self.__account.append(conta)

class User(Client):
    def __init__(self, address, name, document, birthday):
        self.address = address
        self.name = name
        self.document = document
        self.birthday = birthday

class Action:
    def register(action):
        pass
    
teste = Client()
teste.action_register()
teste.register_client('Rua 1')

print(teste.address)
