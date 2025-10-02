# uso de método abstrato
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau"
    
# animal = Animal()  # Isso causará um erro, pois não podemos instanciar uma classe abstrata
cachorro = Cachorro()
gato = Gato()
print(cachorro.fazer_som())  # Saída: Au Au
print(gato.fazer_som())      # Saída: Miau
# animal.fazer_som()  # Isso também causará um erro, pois o método é abstrato
# aula sobre método abstrato
# método abstrato é um método que é declarado, mas não implementado na classe base
# uma classe que contém um método abstrato não pode ser instanciada diretamente
# uma classe que herda de uma classe abstrata deve implementar todos os métodos abstratos
# caso contrário, a subclasse também será considerada abstrata e não poderá ser instanciada
# para definir um método abstrato, usamos o decorador @abstractmethod da biblioteca abc
# abc significa Abstract Base Class (Classe Base Abstrata)
# uma classe abstrata pode conter métodos concretos (com implementação) e métodos abstratos (sem implementação)
# o objetivo dos métodos abstratos é definir uma interface que as subclasses devem seguir
# isso é útil para garantir que todas as subclasses implementem certos métodos

# exemplo de uso de método abstrato
class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "O carro está acelerando"

    def frear(self):
        return "O carro está freando"

class Bicicleta(Veiculo):
    def acelerar(self):
        return "A bicicleta está acelerando"

    def frear(self):
        return "A bicicleta está freando"
    
carro = Carro()
bicicleta = Bicicleta()
print(carro.acelerar())      # Saída: O carro está acelerando
print(carro.frear())        # Saída: O carro está freando
print(bicicleta.acelerar())  # Saída: A bicicleta está acelerando
print(bicicleta.frear())     # Saída: A bicicleta está freando
# veiculo = Veiculo()  # Isso causará um erro, pois não podemos instanciar uma classe abstrata
# veiculo.acelerar()    # Isso também causará um erro, pois o método é abstrato
# veiculo.frear()      # Isso também causará um erro, pois o método é abstrato
  

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        return "A pessoa está falando"
    @abstractmethod
    def andar(self):
        return "A pessoa está andando"
    @abstractmethod
    def comer(self):
        return "A pessoa está comendo"
    
class funcionario(Pessoa):
    def falar(self):
        return super().falar()
    def andar(self):
        return super().andar()
    def comer(self):
        return super().comer()
    def trabalhar(self):
        return "O funcionário está trabalhando"

class aluno(Pessoa):
    def falar(self):
        return super().falar()
    def andar(self):
        return super().andar()
    def comer(self):
        return super().comer()
    def estudar(self):
        return "O aluno está estudando"

funcionario = funcionario()
aluno = aluno()
print(funcionario.falar())
print(funcionario.andar())
print(funcionario.comer())
print(aluno.falar())
print(aluno.andar())
print(aluno.comer())
print(funcionario.trabalhar())
print(aluno.estudar())
# pessoa = Pessoa()  # Isso causará um erro, pois não podemos instanciar

    