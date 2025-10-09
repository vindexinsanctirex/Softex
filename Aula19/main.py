print("=== 1. ASSOCIAÇÃO: Pessoa e Livro ===")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_lido = None  # Associação: Pessoa pode ter um Livro
    
    def ler_livro(self, livro):
        self.livro_lido = livro
        return f"{self.nome} está lendo {livro}"
    
    def __str__(self):
        if self.livro_lido:
            return f"{self.nome} está lendo {self.livro_lido}"
        return f"{self.nome} não está lendo nenhum livro"

# Demonstração
livro1 = Livro("Dom Casmurro", "Machado de Assis")
pessoa1 = Pessoa("João")

print(pessoa1.ler_livro(livro1))  # João está lendo 'Dom Casmurro' por Machado de Assis
print(pessoa1)  # João está lendo 'Dom Casmurro' por Machado de Assis

print("\n=== 2. ASSOCIAÇÃO: Aluno e Ônibus ===")

class Onibus:
    def __init__(self, numero, linha):
        self.numero = numero
        self.linha = linha
    
    def __str__(self):
        return f"Ônibus {self.numero} - Linha {self.linha}"

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def pegar_onibus(self, onibus):
        return f"{self.nome} pegou o {onibus}"
    
    def estudar_no_onibus(self, onibus):
        return f"{self.nome} está estudando no {onibus}"

# Demonstração
onibus_escolar = Onibus(123, "Escolar")
aluno = Aluno("Maria")

print(aluno.pegar_onibus(onibus_escolar))        # Maria pegou o Ônibus 123 - Linha Escolar
print(aluno.estudar_no_onibus(onibus_escolar))   # Maria está estudando no Ônibus 123 - Linha Escolar

print("\n=== 3. AGREGAÇÃO: Departamento e Funcionario ===")

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    def __str__(self):
        return f"{self.nome} ({self.cargo})"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []  # Agregação: lista de funcionários existentes
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        return f"{funcionario.nome} adicionado ao departamento {self.nome}"
    
    def listar_funcionarios(self):
        if not self.funcionarios:
            return f"Departamento {self.nome} não tem funcionários"
        
        lista = f"Funcionários do departamento {self.nome}:\n"
        for func in self.funcionarios:
            lista += f"  - {func}\n"
        return lista

# Demonstração
func1 = Funcionario("Carlos", "Analista")
func2 = Funcionario("Ana", "Gerente")
func3 = Funcionario("Pedro", "Desenvolvedor")

rh = Departamento("Recursos Humanos")
ti = Departamento("Tecnologia da Informação")

rh.adicionar_funcionario(func1)
rh.adicionar_funcionario(func2)
ti.adicionar_funcionario(func3)

print(rh.listar_funcionarios())
print(ti.listar_funcionarios())

# Funcionários continuam existindo independentemente do departamento
print(f"\nFuncionário independente: {func1}")

print("\n=== 4. AGREGAÇÃO: Time e Jogador ===")

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
    
    def __str__(self):
        return f"{self.nome} ({self.posicao})"

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []  # Agregação: lista de jogadores existentes
    
    def contratar_jogador(self, jogador):
        self.jogadores.append(jogador)
        return f"{jogador.nome} contratado pelo {self.nome}"
    
    def escalacao(self):
        if not self.jogadores:
            return f"Time {self.nome} não tem jogadores"
        
        escalacao = f"Escalação do {self.nome}:\n"
        for jogador in self.jogadores:
            escalacao += f"  - {jogador}\n"
        return escalacao

# Demonstração
jogador1 = Jogador("Neymar", "Atacante")
jogador2 = Jogador("Casemiro", "Volante")
jogador3 = Jogador("Alisson", "Goleiro")

brasil = Time("Seleção Brasileira")
brasil.contratar_jogador(jogador1)
brasil.contratar_jogador(jogador2)
brasil.contratar_jogador(jogador3)

print(brasil.escalacao())

print("\n=== 5. COMPOSIÇÃO: Carro e Motor ===")

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        return "Motor ligado"
    
    def desligar(self):
        self.ligado = False
        return "Motor desligado"
    
    def __str__(self):
        status = "ligado" if self.ligado else "desligado"
        return f"Motor {self.potencia}cv - {status}"
    
    def __del__(self):
        print(f"Motor {self.potencia}cv sendo destruído")

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # Composição: Motor criado dentro do Carro
    
    def ligar_carro(self):
        return f"{self.modelo}: {self.motor.ligar()}"
    
    def desligar_carro(self):
        return f"{self.modelo}: {self.motor.desligar()}"
    
    def __str__(self):
        return f"{self.modelo} com {self.motor}"
    
    def __del__(self):
        print(f"Carro {self.modelo} sendo destruído")

# Demonstração
print("Criando carro...")
carro = Carro("Fusca", 65)
print(carro.ligar_carro())  # Fusca: Motor ligado
print(carro)  # Fusca com Motor 65cv - ligado

print("\nDeletando carro...")
del carro  # Motor será destruído automaticamente

print("\n=== 6. COMPOSIÇÃO: Casa e Cômodos ===")

class Comodo:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area
    
    def __str__(self):
        return f"{self.nome} ({self.area}m²)"
    
    def __del__(self):
        print(f"Cômodo {self.nome} sendo destruído")

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []  # Composição: cômodos criados dentro da casa
    
    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)  # Composição: cômodo criado dentro da casa
        self.comodos.append(comodo)
        return f"Cômodo {nome} adicionado à casa"
    
    def area_total(self):
        total = sum(comodo.area for comodo in self.comodos)
        return f"Área total da casa: {total}m²"
    
    def listar_comodos(self):
        if not self.comodos:
            return f"Casa em {self.endereco} não tem cômodos"
        
        lista = f"Cômodos da casa em {self.endereco}:\n"
        for comodo in self.comodos:
            lista += f"  - {comodo}\n"
        return lista
    
    def __del__(self):
        print(f"Casa em {self.endereco} sendo destruída")

# Demonstração
print("\nCriando casa...")
minha_casa = Casa("Rua das Flores, 123")
minha_casa.adicionar_comodo("Sala", 20)
minha_casa.adicionar_comodo("Cozinha", 15)
minha_casa.adicionar_comodo("Quarto", 12)
minha_casa.adicionar_comodo("Banheiro", 6)

print(minha_casa.listar_comodos())
print(minha_casa.area_total())

print("\nDeletando casa...")
del minha_casa  # Todos os cômodos serão destruídos automaticamente

print("\n=== RESUMO DOS RELACIONAMENTOS ===")
print("ASSOCIAÇÃO: Relação fraca entre objetos independentes")
print("AGREGAÇÃO: Relação 'tem-um' onde objetos podem existir separadamente") 
print("COMPOSIÇÃO: Relação 'parte-de' onde objetos dependem do objeto principal")