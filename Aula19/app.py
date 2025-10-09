from abc import ABC, abstractmethod

print("=== 1. DEFINIÇÃO DE CLASSE ABSTRATA ===")

# Classe abstrata
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

# Classes concretas
class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

# Uso das classes
cachorro = Cachorro()
gato = Gato()

print(cachorro.falar())  # Au au!
print(gato.falar())      # Miau!

print("\n=== 2. PROIBIÇÃO DE INSTANCIAMENTO ===")

# Tentativa de instanciar a classe abstrata
try:
    animal = Animal()  # Isso gerará um erro
except TypeError as e:
    print(f"Erro: {e}")

print("\n=== 3. MÚLTIPLOS MÉTODOS ABSTRATOS ===")

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

# Teste
retangulo = Retangulo(5, 3)
print(f"Área: {retangulo.area()}")           # Área: 15
print(f"Perímetro: {retangulo.perimetro()}") # Perímetro: 16

print("\n=== 4. HERANÇA PARCIAL ===")

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def parar(self):
        pass

# Versão INCORRETA (gera erro)
class CarroIncompleto(Transporte):
    def mover(self):
        return "Carro em movimento"

# Tentativa de instanciar (gera erro)
print("Tentativa com classe incompleta:")
try:
    carro_erro = CarroIncompleto()
except TypeError as e:
    print(f"Erro: {e}")

# Versão CORRETA
class Carro(Transporte):
    def mover(self):
        return "Carro em movimento"
    
    def parar(self):
        return "Carro parado"

# Agora funciona
print("\nTentativa com classe completa:")
carro = Carro()
print(carro.mover())  # Carro em movimento
print(carro.parar())  # Carro parado

print("\n=== RESUMO ===")
print("✓ Classes abstratas não podem ser instanciadas")
print("✓ Métodos abstratos devem ser implementados por todas as subclasses")
print("✓ ABC e @abstractmethod são usados para criar classes abstratas")