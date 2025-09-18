# exemplos de herança em POO

class Animal:
    def __init__(self, nome, idade=0, especie="Desconhecida", peso=0.0):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.peso = peso

    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")
    
    def __str__(self):
        return f"Animal: {self.nome} ({self.especie}), Idade: {self.idade}, Peso: {self.peso}kg"
    
class Cachorro(Animal):
    def __init__(self, nome, idade=0, peso=0.0):
        super().__init__(nome, idade, especie="Cachorro", peso=peso)
    
    def fazer_som(self):
        return "Au Au"
    
    def correr(self):
        return "está roendo osso!"
    
class Gato(Animal):
    def __init__(self, nome, idade=0, peso=0.0):
        super().__init__(nome, idade, especie="Gato", peso=peso)
    
    def fazer_som(self):
        return "Miau"
    
    def arranhar(self):
        return "está ronronando!"

class Vaca(Animal):
    def __init__(self, nome, idade=0, peso=0.0):
        super().__init__(nome, idade, especie="Vaca", peso=peso)
    
    def fazer_som(self):
        return "Muu"
    
    def pastar(self):
        return "está pastando!"
    
# criando instâncias das subclasses
cachorro = Cachorro("Rex", 3, 20.5)
gato = Gato("Mimi", 2, 5.0)
vaca = Vaca("Mimosa", 5, 150.0)

# heranças multiplas
class AnimalDeEstimacao:
    def brincar(self):
        return f"{self.nome} está brincando!"

class CachorroDeEstimacao(Cachorro, AnimalDeEstimacao):
    def __init__(self, nome, idade=0, peso=0.0):
        super().__init__(nome, idade, peso)

# criando instância de cachorro de estimação
cachorro_estimacao = CachorroDeEstimacao("Buddy", 4, 22.0)
print(cachorro_estimacao.brincar())  # cachorro brincando
print(cachorro_estimacao.fazer_som())  # som do cachorro

# exibindo
print(f"{cachorro.nome} faz: {cachorro.fazer_som()} e {cachorro.correr()}, {cachorro}")
print(f"{gato.nome} faz: {gato.fazer_som()} e {gato.arranhar()}, {gato}")
print(f"{vaca.nome} faz: {vaca.fazer_som()} e {vaca.pastar()}, {vaca}")

print("\n" + "="*50 + "\n")

# outros exemplos de herança

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        return f"O {self.modelo} está acelerando."

    def frear(self):
        return f"O {self.modelo} está freando."

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()} - Portas: {self.portas}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"

# criando instâncias das subclasses
carro = Carro("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CB500", 2019, "Esportiva")

print(carro.acelerar())
print(moto.frear())
print(carro)
print(moto)

print("\n" + "="*50 + "\n")

# SOLUÇÃO CORRETA PARA HERANÇA MÚLTIPLA

class VeiculoEletrico:
    def __init__(self, capacidade_bateria):
        self.capacidade_bateria = capacidade_bateria  # em kWh

    def carregar(self):
        return f"O veículo está carregando a bateria de {self.capacidade_bateria}kWh."

# Herança múltipla correta - usando composição ou mixin
class CarroEletrico(Carro, VeiculoEletrico):
    def __init__(self, marca, modelo, ano, portas, capacidade_bateria):
        # Inicializa a parte Carro
        Carro.__init__(self, marca, modelo, ano, portas)
        # Inicializa a parte VeiculoEletrico
        VeiculoEletrico.__init__(self, capacidade_bateria)

    def __str__(self):
        return f"{Carro.__str__(self)} - Bateria: {self.capacidade_bateria}kWh"

# Alternativa mais simples: herança única com extensão
class CarroEletricoSimples(Carro):
    def __init__(self, marca, modelo, ano, portas, capacidade_bateria):
        super().__init__(marca, modelo, ano, portas)
        self.capacidade_bateria = capacidade_bateria

    def carregar(self):
        return f"O {self.modelo} está carregando a bateria de {self.capacidade_bateria}kWh."

    def __str__(self):
        return f"{super().__str__()} - Bateria: {self.capacidade_bateria}kWh"

# criando instâncias
print("--- Carro Elétrico com Herança Múltipla ---")
carro_eletrico = CarroEletrico("Tesla", "Model S", 2022, 4, 100)
print(carro_eletrico)
print(carro_eletrico.carregar())
print(carro_eletrico.acelerar())

print("\n--- Carro Elétrico Simples ---")
carro_eletrico_simples = CarroEletricoSimples("Nissan", "Leaf", 2021, 4, 60)
print(carro_eletrico_simples)
print(carro_eletrico_simples.carregar())
print(carro_eletrico_simples.frear())

print("\n" + "="*50 + "\n")

# Exemplo adicional: herança multinível
class VeiculoAutonomo:
    def __init__(self, nivel_autonomia):
        self.nivel_autonomia = nivel_autonomia

    def modo_autonomo(self):
        return f"Modo autônomo ativado (Nível {self.nivel_autonomia})"

class CarroAutonomoEletrico(CarroEletricoSimples, VeiculoAutonomo):
    def __init__(self, marca, modelo, ano, portas, capacidade_bateria, nivel_autonomia):
        CarroEletricoSimples.__init__(self, marca, modelo, ano, portas, capacidade_bateria)
        VeiculoAutonomo.__init__(self, nivel_autonomia)

    def __str__(self):
        return f"{CarroEletricoSimples.__str__(self)} - Autonomia: Nível {self.nivel_autonomia}"

# Testando o carro autônomo elétrico
carro_futurista = CarroAutonomoEletrico("Waymo", "One", 2023, 4, 120, 5)
print("--- Carro Autônomo Elétrico ---")
print(carro_futurista)
print(carro_futurista.carregar())
print(carro_futurista.modo_autonomo())
print(carro_futurista.acelerar())