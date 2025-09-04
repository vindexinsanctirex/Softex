# # exercícios com try, except, else e finally
# def dividir(a, b):
#     try:
#         resultado = a / b
#     except ZeroDivisionError:
#         return "Erro: Divisão por zero não é permitida."
#     except TypeError:
#         return "Erro: Tipos inválidos. Por favor, insira números."
#     else:
#         return f"O resultado da divisão é {resultado}"
#     finally:
#         print("Operação de divisão finalizada.")

# # Testando a função
# print(dividir(10, 2))  # Deve retornar o resultado da divisão
# print(dividir(10, 0))  # Deve retornar erro de divisão por zero
# print(dividir(10, 'a'))  # Deve retornar erro de tipo inválido

# try:
#     num1 = int(input("Digite o primeiro número: "))
#     num2 = int(input("Digite o segundo número: "))
#     resultado = num1 / num2
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")
# else:
#     print(f"O resultado da divisão é {resultado}")

# try:
#     idade = int(input("Digite sua idade: "))
#     if idade <= 0:
#         raise ValueError("Idade deve ser um número positivo.")
#     elif idade > 120 and idade < 1000:
#         raise ValueError("Você é velho demais!")
#     elif idade >= 1000:
#         raise ValueError("Você é imortal?!")
#     else:
#         print(f"Sua idade é {idade} anos.")
# except TypeError:
#     print("Apenas números são permitidos.")

# match input("Digite uma letra: ").lower():
#     case 'a' | 'e' | 'i' | 'o' | 'u':
#         print("Vogal")
#     case _:
#         print("Consoante")

arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()