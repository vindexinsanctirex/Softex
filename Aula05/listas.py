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