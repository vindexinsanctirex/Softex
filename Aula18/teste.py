from functools import reduce

# 1. Dobro dos números (map + lambda)
print("1. Dobro dos números:")
numeros1 = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, numeros1))
print(dobro)  # [2, 4, 6, 8, 10]

# 2. Filtrar pares (filter + lambda)
print("\n2. Filtrar pares:")
numeros2 = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, numeros2))
print(pares)  # [10, 20, 30]

# 3. Soma dos números (reduce + lambda)
print("\n3. Soma dos números:")
numeros3 = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros3)
print(soma)  # 15

# 4. Ordenação por comprimento da palavra (sorted + lambda)
print("\n4. Ordenação por comprimento:")
frutas1 = ["uva", "banana", "maçã", "laranja"]
ordenadas1 = sorted(frutas1, key=lambda palavra: len(palavra))
print(ordenadas1)  # ['uva', 'maçã', 'banana', 'laranja']

# 5. Primeira letra maiúscula (map + lambda)
print("\n5. Primeira letra maiúscula:")
nomes = ["ana", "pedro", "maria"]
maiusculas = list(map(lambda nome: nome.capitalize(), nomes))
print(maiusculas)  # ['Ana', 'Pedro', 'Maria']

# 6. Produto dos números (reduce + lambda)
print("\n6. Produto dos números:")
numeros4 = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, numeros4)
print(produto)  # 120

# 7. Ordenar por último caractere (sorted + lambda)
print("\n7. Ordenar por último caractere:")
frutas2 = ["banana", "uva", "maçã", "laranja"]
ordenadas2 = sorted(frutas2, key=lambda palavra: palavra[-1])
print(ordenadas2)  # ['banana', 'maçã', 'uva', 'laranja']