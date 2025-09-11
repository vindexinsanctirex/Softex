import datetime

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.append((datetime.datetime.now(), 'Depósito', valor))
            print(f'Depositado: R${valor:.2f}')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.historico.append((datetime.datetime.now(), 'Saque', valor))
            print(f'Sacado: R${valor:.2f}')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.__saldo:.2f}')

    def exibir_historico(self):
        print('Histórico de transações:')
        for data, tipo, valor in self.historico:
            print(f'{data.strftime("%d/%m/%Y %H:%M")} - {tipo}: R${valor:.2f}')

    def get_saldo(self):
        return self.__saldo
            

if __name__ == "__main__":
    conta = ContaBancaria('João Silva', 1000)

print(f'Titular: {conta.titular}')
print(f'Saldo inicial: R${conta.get_saldo():.2f}')  
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()
conta.exibir_historico()
conta.sacar(2000)  # Tentativa de saque com saldo insuficiente
conta.depositar(-100)  # Tentativa de depósito com valor negativo   
conta.exibir_historico()
print(f'Saldo atual: R${conta.get_saldo():.2f}')

