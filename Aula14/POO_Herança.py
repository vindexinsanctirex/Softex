# 1. Classe Usuario base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}"
    
    def saudacao(self):
        return "Olá, usuário"

# 2. Classe Cliente que herda de Usuario
class Cliente(Usuario):
    def __init__(self, nome, email, saldo=0):
        super().__init__(nome, email)  # Chama o construtor da classe pai
        self.saldo = saldo
    
    # Método herdado - não precisa sobrescrever
    # exibir_informacoes() será herdado automaticamente
    
    def saudacao(self):  # Sobrescrevendo o método
        return "Olá, cliente"
    
    def exibir_informacoes_completas(self):
        return f"{super().exibir_informacoes()}, Saldo: R${self.saldo:.2f}"

# 3. Classes para herança múltipla
class Autenticacao:
    def login(self):
        return "Usuário autenticado"
    
    def status(self):
        return "Status da autenticação: Ativo"

class Permissao:
    def verificar_permissao(self):
        return "Permissão verificada"
    
    def status(self):
        return "Status da permissão: Concedida"

# 4. Classe Administrador com herança múltipla
class Administrador(Autenticacao, Permissao):
    def __init__(self, nome, email, nivel_acesso):
        self.nome = nome
        self.email = email
        self.nivel_acesso = nivel_acesso
    
    def exibir_info_admin(self):
        return f"Admin: {self.nome}, Nível: {self.nivel_acesso}"

# 5. Hierarquia de classes: Usuario -> Funcionario -> Gerente
class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario
    
    def saudacao(self):
        return "Olá, funcionário"

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, departamento):
        super().__init__(nome, email, salario)
        self.departamento = departamento
    
    def saudacao(self):
        return "Olá, gerente"
    
    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()}, Salário: R${self.salario:.2f}, Departamento: {self.departamento}"

# Demonstração do código
if __name__ == "__main__":
    print("=== DEMONSTRAÇÃO DA HERANÇA ===")
    
    # 1. Cliente herdando de Usuario
    print("\n1. Cliente herdando de Usuario:")
    cliente = Cliente("João Silva", "joao@email.com", 1500.50)
    print(f"Atributos: {cliente.nome}, {cliente.email}, {cliente.saldo}")
    print(f"Método herdado: {cliente.exibir_informacoes()}")
    print(f"Método sobrescrito: {cliente.saudacao()}")
    
    # 2. Funcionario e Gerente
    print("\n2. Hierarquia Usuario -> Funcionario -> Gerente:")
    gerente = Gerente("Maria Santos", "maria@empresa.com", 5000.00, "Vendas")
    print(f"Atributos do gerente: {gerente.nome}, {gerente.email}, {gerente.salario}, {gerente.departamento}")
    print(f"Método exibir_informacoes: {gerente.exibir_informacoes()}")
    print(f"Método saudacao: {gerente.saudacao()}")
    
    # 3. Herança múltipla
    print("\n3. Herança múltipla (Administrador):")
    admin = Administrador("Admin User", "admin@empresa.com", "Super")
    print(f"Método de Autenticacao: {admin.login()}")
    print(f"Método de Permissao: {admin.verificar_permissao()}")
    print(f"Método status (resolução MRO): {admin.status()}")
    
    # 4. Mostrar MRO (Method Resolution Order)
    print("\n4. Ordem de resolução de métodos (MRO):")
    print(f"MRO do Administrador: {Administrador.__mro__}")
    
    # 5. Demonstração do polimorfismo
    print("\n5. Polimorfismo com diferentes tipos de usuários:")
    usuarios = [
        Usuario("Usuário Genérico", "user@email.com"),
        Cliente("Cliente Especial", "cliente@email.com", 2000),
        Funcionario("Funcionário", "func@empresa.com", 3000),
        Gerente("Gerente Geral", "gerente@empresa.com", 7000, "TI")
    ]
    
    for usuario in usuarios:
        print(f"{usuario.saudacao()} - {usuario.exibir_informacoes()}")