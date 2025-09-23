class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = max(0, saldo_inicial)  # Garante que saldo não seja negativo
    
    # Getter para saldo
    @property
    def saldo(self):
        return self._saldo
    
    # Setter para saldo
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Erro: Saldo não pode ser negativo. Operação cancelada.")
    
    # Método para depositar
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Erro: Valor de depósito deve ser positivo.")
    
    # Método para sacar
    def sacar(self, valor):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
            else:
                print("Erro: Saldo insuficiente para o saque.")
        else:
            print("Erro: Valor de saque deve ser positivo.")
    
    def exibir_informacoes(self):
        return f"Titular: {self.titular}, Saldo: R${self._saldo:.2f}"


class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = self._validar_cpf(cpf)
        self._identidade = self._validar_identidade(identidade)
    
    # Métodos de validação
    def _validar_cpf(self, cpf):
        """Validação básica de CPF (apenas verifica se tem 11 dígitos)"""
        cpf_str = str(cpf).replace('.', '').replace('-', '')
        if len(cpf_str) == 11 and cpf_str.isdigit():
            return cpf
        else:
            raise ValueError("CPF deve conter 11 dígitos numéricos")
    
    def _validar_identidade(self, identidade):
        """Validação básica de identidade"""
        identidade_str = str(identidade).replace('.', '').replace('-', '')
        if identidade_str.isdigit() and len(identidade_str) >= 5:
            return identidade
        else:
            raise ValueError("Identidade deve conter pelo menos 5 dígitos numéricos")
    
    # Getter e Setter para CPF
    @property
    def cpf(self):
        # Retorna o CPF formatado
        cpf_str = str(self._cpf).zfill(11)
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = self._validar_cpf(novo_cpf)
    
    # Getter e Setter para Identidade
    @property
    def identidade(self):
        return self._identidade
    
    @identidade.setter
    def identidade(self, nova_identidade):
        self._identidade = self._validar_identidade(nova_identidade)
    
    # Método para exibir informações formatadas
    def exibir_informacoes(self):
        return (f"Nome: {self.nome}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"CPF: {self.cpf}\n"
                f"Identidade: {self.identidade}")
    
    # Método para obter CPF sem formatação (apenas números)
    def get_cpf_numerico(self):
        return str(self._cpf).zfill(11)


# Demonstração do código
if __name__ == "__main__":
    print("=== DEMONSTRAÇÃO DA CLASSE CONTA BANCÁRIA ===")
    
    # Testando ContaBancaria
    conta = ContaBancaria("João Silva", 1000)
    print(conta.exibir_informacoes())
    
    # Testando operações
    conta.depositar(500)
    conta.sacar(200)
    
    # Tentando operações inválidas
    conta.sacar(2000)  # Saldo insuficiente
    conta.depositar(-100)  # Valor negativo
    
    # Testando setter do saldo
    print("\nTestando setter do saldo:")
    conta.saldo = 1500  # Válido
    print(f"Novo saldo: R${conta.saldo:.2f}")
    
    conta.saldo = -500  # Inválido - não altera o saldo
    print(f"Saldo após tentativa inválida: R${conta.saldo:.2f}")
    
    print("\n" + "="*50)
    print("=== DEMONSTRAÇÃO DA CLASSE PESSOA ===")
    
    # Testando Pessoa
    pessoa = Pessoa("Maria Santos", "15/03/1990", "12345678901", "1234567")
    print(pessoa.exibir_informacoes())
    
    # Testando getters e setters
    print("\nTestando getters e setters:")
    print(f"CPF formatado: {pessoa.cpf}")
    print(f"CPF numérico: {pessoa.get_cpf_numerico()}")
    print(f"Identidade: {pessoa.identidade}")
    
    # Alterando CPF e Identidade
    pessoa.cpf = "98765432109"
    pessoa.identidade = "7654321"
    print(f"\nApós alteração:")
    print(f"Novo CPF: {pessoa.cpf}")
    print(f"Nova Identidade: {pessoa.identidade}")
    
    # Testando validações
    print("\nTestando validações:")
    try:
        pessoa_invalida = Pessoa("Teste", "01/01/2000", "123", "123")  # CPF inválido
    except ValueError as e:
        print(f"Erro ao criar pessoa: {e}")
    
    try:
        pessoa.cpf = "123"  # CPF inválido
    except ValueError as e:
        print(f"Erro ao alterar CPF: {e}")


# Exemplo adicional: Integrando as duas classes
class ContaBancariaComTitular(ContaBancaria):
    def __init__(self, pessoa, saldo_inicial=0):
        super().__init__(pessoa.nome, saldo_inicial)
        self.pessoa = pessoa
    
    def exibir_informacoes_completas(self):
        return (f"{self.pessoa.exibir_informacoes()}\n"
                f"Saldo da conta: R${self.saldo:.2f}")


# Demonstração da integração
print("\n" + "="*50)
print("=== INTEGRAÇÃO DAS CLASSES ===")

pessoa_titular = Pessoa("Carlos Oliveira", "20/07/1985", "11122233344", "9876543")
conta_integrada = ContaBancariaComTitular(pessoa_titular, 5000)

print(conta_integrada.exibir_informacoes_completas())

