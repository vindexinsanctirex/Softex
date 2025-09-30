# # exemplos básicos de lambda

# # função tradicional
# def soma(x, y):
#     return x + y

# # função lambda
# soma_lambda = lambda x, y: x + y

# # uso de lambda com map
# numeros = [1, 2, 3, 4, 5]
# quadrados = list(map(lambda x: x**2, numeros))
# print(quadrados)  # Output: [1, 4, 9, 16, 25]

# # uso de lambda com filter
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)  # Output: [2, 4]

# # uso de lambda com sorted
# pessoas = [{'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 20}, {'nome': 'Carlos', 'idade': 30}]
# pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa['idade'])
# print(pessoas_ordenadas)  # Output: [{'nome': 'Bruno', 'idade': 20}, {'nome': 'Ana', 'idade': 25}, {'nome': 'Carlos', 'idade': 30}]

# # uso de lambda com reduce
# from functools import reduce
# soma_total = reduce(lambda x, y: x + y, numeros)
# print(soma_total)  # Output: 15

# # lambda em funções de ordem superior
# def aplicar_operacao(x, y, operacao):
#     return operacao(x, y)

# resultado = aplicar_operacao(10, 5, lambda a, b: a * b)
# print(resultado)  # Output: 50

# def mutiplica_lista(lista, funcao):
#     for index, item in enumerate(lista):
#         lista[index] = funcao(item)
#     return lista

# def dobra(x):
#     return x * 2

# print(mutiplica_lista([1, 2, 3, 4], dobra))  # Output: [2, 4, 6, 8]

# print(mutiplica_lista([1, 2, 3, 4], lambda x: x * 3))  # Output: [3, 6, 9, 12]

# # map, filter, reduce com lambda
# from functools import reduce
# numeros = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x * 2, numeros)))          # Output: [2, 4, 6, 8, 10]
# print(list(filter(lambda x: x % 2 == 0, numeros)))   # Output: [2, 4]
# print(reduce(lambda x, y: x + y, numeros))            # Output: 15

# # map e list map
# numeros = [1, 2, 3, 4, 5]
# dobrados = list(map(lambda x: x * 2, numeros))
# print(dobrados)  # Output: [2, 4, 6, 8, 10]
# # filter e list filter
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)  # Output: [2, 4]
# # reduce
from functools import reduce
# soma = reduce(lambda x, y: x + y, numeros)
# print(soma)  # Output: 15

#dict map lambda
pessoas = [{'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 20}, {'nome': 'Carlos', 'idade': 30}]
nomes = list(map(lambda pessoa: pessoa['nome'], pessoas))
print(nomes)  # Output: ['Ana', 'Bruno', 'Carlos']
print(dict(map(lambda pessoa: (pessoa['nome'], pessoa['idade']), pessoas)))  # Output: {'Ana': 25, 'Bruno': 20, 'Carlos': 30}

lista = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, lista))  # Output: 120 (1*2*3*4*5)

lista = ['Jacara', 'Abacaxi', 'Laranja', 'Banana']
print(reduce(lambda x, y : x + ' ' + y, lista))  # Output: 'Jacara Abacaxi Laranja Banana'