# num = input("Digite um número de 1 a 5: ")
# match num:
#     case "1":
#         print("Um")
#     case "2":
#         print("Dois")
#     case "3":
#         print("Três")
#     case "4":
#         print("Quatro")
#     case "5":
#         print("Cinco")
#     case _:
#         print("Número inválido")

# # ou
# num = int(input("Digite um número de 1 a 5: "))
# match num:
#     case 1 | 2 | 3 | 4 | 5:
#         print(f"Você digitou o número {num}")
#     case _:
#         print("Número inválido")


# # agora pra achar par ou ímpar entre os números de 1 a 5
# num = int(input("Digite um número de 1 a 5: "))
# match num:
#     case 1 | 2 | 3 | 4 | 5 if num % 2 == 0:
#         print(f"O número {num} é par")
#     case 1 | 2 | 3 | 4 | 5 if num % 2 != 0:
#         print(f"O número {num} é ímpar")
#     case _  :
#         print("Número inválido")

# agora com opções de adicionar, editar, pesquisar e deletar digitando números para acessar as opções
# op = int(input("Digite a opção desejada:\n1 - Adicionar\n2 - Editar\n3 - Pesquisar\n4 - Deletar\n5 - Sair\n"))
# match op:
#     case 1:
#         print("Adicionar")
#     case 2:
#         print("Editar")
#     case 3:
#         print("Pesquisar")
#     case 4:
#         print("Deletar")
#     case 5:
#         print("Sair")
#     case _:
#         print("Opção inválida")

# def ola (msg, nome):
#     return f"Grande {msg}, {nome}!"
# print(ola("dia", "João"))

# def soma (a, b):
#     valor_somado = a + b
#     return valor_somado
# valor = soma(2, 3)
# print(f"A soma é {valor}")

def adiciona_livro(titulo, autor, ano):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }
    return livro

livro1 = adiciona_livro("1984", "George Orwell", 1949)
livro2 = adiciona_livro("To Kill a Mockingbird", "Harper Lee", 1960)
print(livro1)
print(livro2)

def exibir_livro(livro):
    print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

def soma(num1, num2):
    global resultado
    resultado = num1 + num2
    return resultado

# Primeira chamada
valor1 = soma(5, 7)
print(f"Valor1: {valor1}")           # 12
print(f"Resultado: {resultado}")     # 12

# Segunda chamada - A VARIÁVEL GLOBAL É SOBRESCRITA!
valor2 = soma(10, 3)
print(f"Valor2: {valor2}")           # 13
print(f"Resultado: {resultado}")     # 13 (agora vale 13!)

# Terceira chamada
valor3 = soma(100, 50)
print(f"Valor3: {valor3}")           # 150
print(f"Resultado: {resultado}")     # 150 (agora vale 150!)