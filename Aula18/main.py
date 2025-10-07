# single responsibility principle
# cada classe deve ter uma única responsabilidade
# uma classe deve ter apenas um motivo para mudar
# exemplo:
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito: {valor}")
        print(f"Depósito de {valor} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: {valor}")
            print(f"Saque de {valor} realizado com sucesso.")
    def extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for item in self.historico:
            print(item)
        print(f"Saldo atual: {self.saldo}")
class GerenciadorContas:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        for conta in self.contas:
            print(f"Titular: {conta.titular}, Saldo: {conta.saldo}")
# uso
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)

gerenciador = GerenciadorContas()
gerenciador.adicionar_conta(conta1)
gerenciador.adicionar_conta(conta2)

gerenciador.listar_contas()
conta1.depositar(200)
conta1.sacar(150)
conta1.extrato()
conta2.sacar(600)
conta2.extrato()
# nesse exemplo, a classe ContaBancaria é responsável apenas por gerenciar as operações da conta,
# enquanto a classe GerenciadorContas é responsável por gerenciar múltiplas contas.
# assim, cada classe tem uma única responsabilidade e um único motivo para mudar.

# open/closed principle
# classes devem estar abertas para extensão, mas fechadas para modificação
# exemplo:
from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio ** 2
    def perimetro(self):
        return 2 * 3.14 * self.raio
    
# uso
formas = [Retangulo(4, 5), Circulo(3)]
for forma in formas:
    print(f"Área: {forma.area()}, Perímetro: {forma.perimetro()}")
# nesse exemplo, a classe FormaGeometrica é uma classe abstrata que define a interface
# para todas as formas geométricas. As classes Retangulo e Circulo estendem essa classe
# e implementam os métodos area e perimetro. Se quisermos adicionar uma nova forma geométrica,
# podemos criar uma nova classe que estende FormaGeometrica sem modificar as classes existentes.
# assim, as classes estão abertas para extensão (podemos adicionar novas formas geométricas),
# mas fechadas para modificação (não precisamos alterar as classes existentes).

# Liskov substitution principle
# objetos de uma classe derivada devem poder substituir objetos da classe base sem alterar o funcionamento do   programa
# exemplo:
class Ave(ABC):
    @abstractmethod
    def voar(self):
        pass
    @abstractmethod
    def cantar(self):
        pass

class Pardal(Ave):
    def voar(self):
        print("Pardal voando")
    def cantar(self):
        print("Pardal cantando")

class Pinguim(Ave):
    def voar(self):
        raise NotImplementedError("Pinguins não podem voar")
    def cantar(self):
        print("Pinguim cantando")

# uso
def fazer_ave_voar(ave):
    ave.voar()
    ave.cantar()
pardal = Pardal()
fazer_ave_voar(pardal)
pinguim = Pinguim()
# fazer_ave_voar(pinguim)  # isso vai gerar um erro
# nesse exemplo, a classe Ave define a interface para todas as aves, incluindo os métodos voar e cantar.
# A classe Pardal implementa ambos os métodos, mas a classe Pinguim não pode voar.
# Quando tentamos fazer um Pinguim voar, isso gera um erro, o que viola o princípio de substituição de Liskov.
# para corrigir isso, poderíamos criar uma interface separada para aves que podem voar
# e outra para aves que não podem voar, garantindo que todas as subclasses possam ser substituídas sem problemas. 
# assim, objetos de uma classe derivada (Pardal) podem substituir objetos da classe base (Ave)
# sem alterar o funcionamento do programa, mas objetos de outra classe derivada (Pinguim) não podem.
# isso mostra a importância de projetar hierarquias de classes que respeitem o princípio de substituição de Liskov.

# interface segregation principle
# muitas interfaces específicas são melhores do que uma interface única e geral
# exemplo:
class Impressora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass
    @abstractmethod
    def escanear(self, documento):
        pass
    @abstractmethod
    def fax(self, documento):
        pass

class ImpressoraSimples(Impressora):
    def imprimir(self, documento):
        print(f"Imprimindo: {documento}")
    def escanear(self, documento):
        raise NotImplementedError("Essa impressora não pode escanear")
    def fax(self, documento):
        raise NotImplementedError("Essa impressora não pode enviar fax")

class ImpressoraMultifuncional(Impressora):
    def imprimir(self, documento):
        print(f"Imprimindo: {documento}")
    def escanear(self, documento):
        print(f"Escaneando: {documento}")
    def fax(self, documento):
        print(f"Enviando fax: {documento}")

# uso
impressora1 = ImpressoraSimples()
impressora1.imprimir("Documento 1")
# impressora1.escanear("Documento 1")  # isso vai gerar um erro
impressora2 = ImpressoraMultifuncional()
impressora2.imprimir("Documento 2")
impressora2.escanear("Documento 2")
impressora2.fax("Documento 2")
# nesse exemplo, a interface Impressora define três métodos: imprimir, escanear e fax.
# A classe ImpressoraSimples implementa apenas o método imprimir, enquanto a classe ImpressoraMultifuncional implementa todos os três métodos.
# Quando tentamos usar o método escanear em uma ImpressoraSimples, isso gera um erro,
# o que viola o princípio de segregação de interfaces.
# para corrigir isso, poderíamos criar interfaces separadas para cada funcionalidade (Impressora, Scanner, Fax),
# garantindo que as classes só precisem implementar os métodos que realmente usam.
# assim, muitas interfaces específicas são melhores do que uma interface única e geral.

# dependency inversion principle
# módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
# abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.
# exemplo:
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, dados):
        pass

class RepositorioSQL(Repositorio):
    def salvar(self, dados):
        print(f"Salvando dados no banco SQL: {dados}")

class RepositorioNoSQL(Repositorio):
    def salvar(self, dados):
        print(f"Salvando dados no banco NoSQL: {dados}")

# uso
repositorio1 = RepositorioSQL()
repositorio1.salvar("Dados do usuário")

repositorio2 = RepositorioNoSQL()
repositorio2.salvar("Dados do produto")
# nesse exemplo, a classe Repositorio é uma abstração que define o método salvar.
# As classes RepositorioSQL e RepositorioNoSQL implementam essa abstração,
# permitindo que o código de alto nível (o uso dos repositórios) dependa da abstração (Repositorio)
# em vez de depender dos detalhes (RepositorioSQL ou RepositorioNoSQL).
# assim, módulos de alto nível não dependem de módulos de baixo nível, e ambos dependem de abstrações.
# além disso, as abstrações (Repositorio) não dependem de detalhes (RepositorioSQL ou RepositorioNoSQL),
# mas os detalhes dependem da abstração. isso facilita a manutenção e a extensão do código,
# pois podemos adicionar novos tipos de repositórios (como RepositorioMongoDB) sem alterar o código de alto nível.
# essas são as cinco princípios SOLID de design de software orientado a objetos.
# seguir esses princípios ajuda a criar sistemas mais flexíveis, manuteníveis e escaláveis.
# eles promovem boas práticas de design e ajudam a evitar problemas comuns em sistemas complexos.
# ao aplicar esses princípios, os desenvolvedores podem criar código que é mais fácil de entender,
# modificar e estender ao longo do tempo, resultando em software de alta qualidade.