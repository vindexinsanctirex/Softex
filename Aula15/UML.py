# estudando UML
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}, agora você tem {self.idade} anos!")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} adicionada para o aluno {self.nome}.")

    def calcular_media(self):
        if self.notas:
            media = sum(self.notas) / len(self.notas)
            print(f"A média do aluno {self.nome} é {media:.2f}.")
            return media
        else:
            print(f"O aluno {self.nome} não possui notas.")
            return 0
        
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f"O professor {self.nome} está ensinando {self.disciplina}.")

# Exemplo de uso das classes
if __name__ == "__main__":
    aluno1 = Aluno("João", 20, "2023001")
    aluno1.adicionar_nota(8.5)
    aluno1.adicionar_nota(7.0)
    aluno1.calcular_media()
    aluno1.fazer_aniversario()

    professor1 = Professor("Maria", 35, "Matemática")
    professor1.ensinar()
    professor1.fazer_aniversario()

# associação cardinalidade 1:N
class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} adicionado ao curso {self.nome}.")
        else:
            print("Apenas objetos do tipo Aluno podem ser adicionados.")

    def listar_alunos(self):
        print(f"Alunos no curso {self.nome}:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}, Idade: {aluno.idade}, Matrícula: {aluno.matricula}")

# Exemplo de uso da classe Curso
if __name__ == "__main__":
    curso_python = Curso("Python para Iniciantes")
    curso_python.adicionar_aluno(aluno1)
    curso_python.listar_alunos()

# composição cardinalidade 1:1
class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return f"{self.rua}, {self.cidade} - {self.estado}, CEP: {self.cep}"
    
class PessoaComEndereco(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        if isinstance(endereco, Endereco):
            self.endereco = endereco
        else:
            raise ValueError("endereco deve ser uma instância de Endereco")

    def mostrar_endereco(self):
        print(f"Endereço de {self.nome}: {self.endereco}")

# Exemplo de uso da composição
if __name__ == "__main__":
    endereco_joao = Endereco("Rua A", "Cidade X", "Estado Y", "12345-678")
    pessoa_joao = PessoaComEndereco("João", 20, endereco_joao)
    pessoa_joao.mostrar_endereco()
    pessoa_joao.fazer_aniversario()

# agregação cardinalidade 1:N
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if isinstance(professor, Professor):
            self.professores.append(professor)
            print(f"Professor {professor.nome} adicionado ao departamento {self.nome}.")
        else:
            print("Apenas objetos do tipo Professor podem ser adicionados.")

    def listar_professores(self):
        print(f"Professores no departamento {self.nome}:")
        for professor in self.professores:
            print(f"- {professor.nome}, Idade: {professor.idade}, Disciplina: {professor.disciplina}")

# Exemplo de uso da agregação
if __name__ == "__main__":
    departamento_matematica = Departamento("Matemática")
    departamento_matematica.adicionar_professor(professor1)
    departamento_matematica.listar_professores()

# dependência
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro}' adicionado à biblioteca {self.nome}.")

    def listar_livros(self):
        print(f"Livros na biblioteca {self.nome}:")
        for livro in self.livros:
            print(f"Título: {livro}")

# Exemplo de uso da dependência
if __name__ == "__main__":
    biblioteca_central = Biblioteca("Biblioteca Central")
    biblioteca_central.adicionar_livro("Introdução à Programação")
    biblioteca_central.adicionar_livro("Estruturas de Dados")
    biblioteca_central.adicionar_livro("Contos de Yatar")
    biblioteca_central.listar_livros()