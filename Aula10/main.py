#estudando OOP - Orientação a Objetos
class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    def ligar(self):
        self.__ligada = True

    def desligar(self):
        self.__ligada = False

    def checar_lampada(self):
        return self.__ligada
    def get_voltagem(self):
        return self.__voltagem
    def get_cor(self):
        return self.__cor

lamp1 = Lampada(110, 'Branca')
lamp2 = Lampada(220, 'Amarela')
print(lamp1.get_cor(), lamp1.get_voltagem())
print(lamp2.get_voltagem(), lamp2.get_cor())
lamp1.ligar()
print(lamp1.checar_lampada())
lamp1.desligar()
print(lamp1.checar_lampada())

if lamp1.checar_lampada() == True:
    print('A lampada está ligada')
else:
    print('A lampada está desligada')

class Cachorro:
    especie = 'Canis familiaris' # atributo de classe
    def __init__(self, nome, raca, idade): # método construtor
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __str__(self):
        return f'Espécie: {self.especie} - Nome: {self.nome} - Raça: {self.raca} - Idade: {self.idade}'
    
    def latir(self):
        print('Au Au')

doguinho01 = Cachorro('Rex', 'Dobberman', '2 anos')
# print(doguinho01.especie, doguinho01.nome, doguinho01.raca, doguinho01.idade, sep=' - ')
print(doguinho01)
auau = Cachorro('Toto', 'Caramelo', '1 ano')
print(auau.especie, auau.nome, auau.raca, auau.idade, sep='\n')
doguinho01.latir()
auau.latir()

class Fruta:
    def __init__(self, nome:str, cor:str, sabor:str, peso:float):
        self.nome = nome
        self.cor = cor
        self.sabor = sabor
        self.peso = peso

    def __str__(self):
        return f'Nome: {self.nome} - Cor: {self.cor} - Sabor: {self.sabor} - Peso: {self.peso}'

maca = Fruta('Maçã', 'Vermelha', 'Doce', 0.3)
print(maca)
banana = Fruta('Banana', 'Amarela', 'Doce', 0.25)
print(banana)
uva = Fruta('Uva', 'Roxa', 'Doce', 0.05)
print(uva)
laranja = Fruta('Laranja', 'Laranja', 'Cítrico', 0.4)
print(laranja)

class Esporte:
    def __init__(self, nome:str, time:str, jogadores:int, modalidade:str='Livre'):
        self.nome = nome
        self.time = time
        self.jogadores = jogadores
        self.modalidade = modalidade

    def __str__(self):
        return f'Nome: {self.nome} \n Time: {self.time}  \n  Jogadores: {self.jogadores} \n Modalidade: {self.modalidade}'
    
futebol = Esporte('Futebol', 'Brasil', 11, 'Coletivo')
print(futebol)
volei = Esporte('Vôlei', 'Brasil', 6, 'Coletivo')
print(volei)
xadrez = Esporte('Xadrez', 'Brasil', 1, 'Individual')
print(xadrez)
natação = Esporte('Natação', 'Brasil', 1, 'Individual')
print(natação)
parkour = Esporte('Parkour', 'Brasil', 1)
print(parkour)