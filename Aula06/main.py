# união de listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_unida = lista1 + lista2
print(lista_unida)

# ou
lista_unida = []
for i in lista1:
    lista_unida.append(i)
for i in lista2:
    lista_unida.append(i)
print(lista_unida)

# ou
lista_unida = [*lista1, *lista2]
print(lista_unida)

# união de conjuntos
lista1 = {1, 2, 3}
lista2 = {4, 5, 6}
lista_unida = lista1.union(lista2)
print(lista_unida)

# ou
lista_unida = lista1 | lista2
print(lista_unida)

# ou
lista_unida = { *lista1, *lista2 }
print(lista_unida)

# conjuntos de livros com diferença simétrica, ou seja, que estão em um conjunto ou em outro, mas não em ambos
livros1 = {"O Senhor dos Anéis", "1984", "Fahrenheit 451"}
livros2 = {"1984", "Brave New World", "Fahrenheit 451"}
livros_diferenca_simetrica = livros1.symmetric_difference(livros2)
print(livros_diferenca_simetrica)

# ou
livros_diferenca_simetrica = livros1 ^ livros2
print(livros_diferenca_simetrica)

# ou
livros_diferenca_simetrica = { *livros1, *livros2 } - (livros1 & livros2)
print(livros_diferenca_simetrica)

# conjunto de livros com interseção
livros_interseccao = livros1.intersection(livros2)
print(livros_interseccao)

# ou
livros_interseccao = livros1 & livros2
print(livros_interseccao)