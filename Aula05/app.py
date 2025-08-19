# count = 0
# while True:
#     count += 1
#     print("Hello World")
#     if count == 10:
#         break
# print("Loop finished after 10 iterations.")

# while count < 20:
#     count += 1
#     print("Continuing to print Hello World")
# print("Loop finished after 20 iterations.")


# ## Exercício 1: Conversão de Tipos
# num_str = "123"
# num_int = int(num_str)
# num_float = float(num_int)
# print(num_int)
# print(num_float)

# ## Exercício 2: Operações com Strings
# texto = "Python é incrível!"
# # Contar caracteres
# print(len(texto))
# # Converter para maiúsculas
# print(texto.upper())
# # Substituir palavra
# print(texto.replace("incrível", "poderoso"))

# ## Exercício 3: Listas e Indexação
# numeros = [10, 20, 30, 40, 50]
# # Acessar terceiro elemento (índice 2)
# print(numeros[2])
# # Adicionar 60 no final
# numeros.append(60)
# # Remover o número 20
# numeros.remove(20)
# print(numeros)

# ## Exercício 4: Dicionários
# aluno = {
#     "nome": "Maria",
#     "idade": 22,
#     "curso": "Engenharia"
# }
# # Adicionar chave "notas"
# aluno["notas"] = [8.5, 7.0, 9.2]
# # Imprimir valor da chave "curso"
# print(aluno["curso"])

# ## Exercício 5: Tuplas e Conjuntos
# cores = ("vermelho", "verde", "azul", "verde")
# # Converter para conjunto (remove duplicatas)
# cores_set = set(cores)
# # Adicionar "amarelo"
# cores_set.add("amarelo")
# print(cores_set)

# ## Exercício 6: Operações Matemáticas
# a = 15
# b = 4
# # Divisão inteira
# print(a // b)
# # Resto da divisão
# print(a % b)

# ## Exercício 7: Verificação de Tipos
# dados = [42, 3.14, "Python", True, [1, 2]]
# for elemento in dados:
#     print(type(elemento))

# ## Exercício 8: Manipulação de Strings
# texto = "programação"
# # Inverter string
# invertido = texto[::-1]
# print(invertido)
# # Verificar se é igual ao original
# print(texto == invertido)

# ## Exercício 9: Listas Aninhadas
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Acessar número 5 (linha 1, coluna 1)
# print(matriz[1][1])
# # Substituir 8 por 10
# matriz[2][1] = 10
# print(matriz)

# ## Exercício 10: Desafio Final
# estoque = {
#     "maçã": 10,
#     "banana": 5,
#     "laranja": 8
# }
# # Adicionar "pera"
# estoque["pera"] = 12
# # Remover "banana"
# del estoque["banana"]
# # Imprimir nomes dos itens (chaves)
# print(estoque.keys())

frutas = ["maçã", "banana", "laranja"]
frutas.insert(1, "pera")  # Adiciona "pera" na posição 1
print(frutas)

frutas.append("uva")  # Adiciona "uva" no final
print(frutas)

frutas_vermelhas = ['maçã', 'amora', 'morango', 'cereja']

frutas += frutas_vermelhas  # Adiciona frutas vermelhas à lista
print(frutas)

frutas.remove("maçã")  # Remove "maçã"
print(frutas)

frutas.pop(2)  # Remove o item na posição 2 (laranja)
print(frutas)

frutas.pop()  # Remove o último item (cereja)
print(frutas)

cores = ["vermelho", "verde", "azul"]
cores.insert(0, "amarelo")  # Adiciona "amarelo" na posição 0
print(cores)

cores.append("roxo")  # Adiciona "roxo" no final
print(cores)

print(cores[1:6:2]) # Acessa do índice 1 ao 5, pulando de 2 em 2

cores += frutas

print(cores[-1:-12:-1]) # Acessa do último ao nono elemento, pulando de 1 em 1

print(id(cores))  # Imprime o ID da lista cores
print(id(frutas))  # Imprime o ID da lista frutas

vermelhas = frutas_vermelhas.copy()  # Cria uma cópia da lista frutas_vermelhas
print(vermelhas)

print(id(vermelhas))  # Imprime o ID da lista vermelhas
print(id(frutas_vermelhas))  # Imprime o ID da lista frutas_vermelhas 

print(vermelhas is frutas_vermelhas)  # Verifica se são o mesmo objeto
print(vermelhas == frutas_vermelhas)  # Verifica se têm o mesmo conteúdo

print(sorted(cores))  # Imprime a lista cores ordenada