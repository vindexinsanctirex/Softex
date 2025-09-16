# exemplo de POO
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos." 
    
p1 = Pessoa("João", 30)
print(p1.apresentar())  
p2 = Pessoa("Maria", 25)
print(p2.apresentar())