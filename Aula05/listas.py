# 1) Criar lista com diferentes tipos de dados
lista_mista = ["Python", 42, 3.14, [1, 2, 3], True, {"nome": "João"}]
print("1) Lista mista:", lista_mista)

# 2) Manipular a lista
lista_mista.append("novo elemento")
lista_mista.insert(2, "inserido na posição 2")
lista_mista.remove(42)
print("2) Lista após manipulação:", lista_mista)

# 3) Fazer cópia e verificar IDs
copia_lista = lista_mista.copy()
print("3) ID original:", id(lista_mista))
print("   ID cópia:", id(copia_lista))
print("   São iguais?", id(lista_mista) == id(copia_lista))

# 4) Lista numérica e multiplicação
lista_numeros = [2, 4.5, 7, 10.2, 15]
lista_multiplicada = [numero * 5 for numero in lista_numeros]
print("4) Lista original:", lista_numeros)
print("   Lista multiplicada:", lista_multiplicada)

# 5) Slice para índices 3 e 4
lista_original = [1, 2, 3, 4, 5, 6]
nova_lista = lista_original[3:5]
print("5) Lista original:", lista_original)
print("   Nova lista (índices 3 e 4):", nova_lista)

print(type(lista_mista))
print(lista_original[2])

lista1 = []
for num in range(10):
    if num % 2 == 0:
     lista1.append(num)
print(lista1)

lista2 = [num for num in range(10) if num % 2 == 0]
print(lista2)

matriz = [0 for i in range(3)]
print(matriz)

matriz = [[0 for j in range(3)] for i in range(3)]
print(matriz)

# Criando uma matriz 3x3x3 preenchida com zeros
dimensoes = (3, 3, 3)  # (camadas, linhas, colunas)
matriz_3d = [[[0 for _ in range(dimensoes[2])] 
              for _ in range(dimensoes[1])] 
             for _ in range(dimensoes[0])]
print(matriz_3d)

# Representando coordenadas em um espaço 3D 2x2x2
espaco_3d = [
    # Camada z=0
    [
        ['(0,0,0)', '(0,0,1)'],  # y=0
        ['(0,1,0)', '(0,1,1)']   # y=1
    ],
    # Camada z=1
    [
        ['(1,0,0)', '(1,0,1)'],  # y=0
        ['(1,1,0)', '(1,1,1)']   # y=1
    ]
]

# Encontrando uma coordenada específica
def encontrar_coordenada(x, y, z):
    return espaco_3d[x][y][z]

print(encontrar_coordenada(1, 0, 1))  # Saída: (1,0,1)