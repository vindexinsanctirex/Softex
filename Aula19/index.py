from abc import ABC, abstractmethod

print("=== 1. CRIANDO UMA INTERFACE ===")

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando R${valor:.2f} via Cartão de Crédito"

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Processando R${valor:.2f} via Boleto Bancário"

# Uso das classes
cartao = CartaoCredito()
boleto = Boleto()

print(cartao.processar(150.50))  # Processando R$150.50 via Cartão de Crédito
print(boleto.processar(200.75))  # Processando R$200.75 via Boleto Bancário

print("\n=== 2. INTERFACE MÚLTIPLA ===")

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "Computador ligado"
    
    def desligar(self):
        return "Computador desligado"

# Uso
computador = Computador()
print(computador.ligar())    # Computador ligado
print(computador.desligar()) # Computador desligado

print("\n=== 3. INTERFACE EM HERANÇA MÚLTIPLA ===")

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def __init__(self, titulo):
        self.titulo = titulo
    
    def imprimir(self):
        return f"Imprimindo relatório: {self.titulo}"
    
    def exportar(self):
        return f"Exportando relatório: {self.titulo} para PDF"

# Uso
relatorio = Relatorio("Vendas do Trimestre")
print(relatorio.imprimir())  # Imprimindo relatório: Vendas do Trimestre
print(relatorio.exportar())  # Exportando relatório: Vendas do Trimestre para PDF

print("\n=== 4. FORÇANDO CONTRATO ===")

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    
    @abstractmethod
    def buscar(self, id):
        pass

# Versão INCORRETA (não implementa todos os métodos)
class RepositorioMemoriaIncompleto(Repositorio):
    def salvar(self, objeto):
        return f"Salvando objeto: {objeto}"

# Tentativa de instanciar (gera erro)
print("Tentativa com classe incompleta:")
try:
    repositorio_erro = RepositorioMemoriaIncompleto()
except TypeError as e:
    print(f"Erro: {e}")

# Versão CORRETA
class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}
        self.contador = 1
    
    def salvar(self, objeto):
        id = self.contador
        self.dados[id] = objeto
        self.contador += 1
        return f"Objeto salvo com ID: {id}"
    
    def buscar(self, id):
        if id in self.dados:
            return f"Objeto encontrado: {self.dados[id]}"
        return f"Objeto com ID {id} não encontrado"

# Agora funciona
print("\nTentativa com classe completa:")
repositorio = RepositorioMemoria()
print(repositorio.salvar("Dados importantes"))  # Objeto salvo com ID: 1
print(repositorio.salvar("Outros dados"))       # Objeto salvo com ID: 2
print(repositorio.buscar(1))                    # Objeto encontrado: Dados importantes
print(repositorio.buscar(3))                    # Objeto com ID 3 não encontrado

print("\n=== DEMONSTRAÇÃO DE POLIMORFISMO ===")

print("\nUsando interface Pagamento com diferentes implementações:")
pagamentos = [CartaoCredito(), Boleto()]

for pagamento in pagamentos:
    print(pagamento.processar(100.00))

print("\n=== RESUMO ===")
print("✓ Interfaces em Python são criadas com classes abstratas")
print("✓ Todas as classes devem implementar TODOS os métodos abstratos")
print("✓ Herança múltipla de interfaces é permitida")
print("✓ Interfaces garantem contratos entre classes")
print("✓ TypeError é gerado ao tentar instanciar classes incompletas")