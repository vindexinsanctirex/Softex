# a = [ 0 , 1 ,2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

# print (a[-1])

# print ("Helo" 'word' * 2)

# class test():
#     id = 0
#     def __init__(self, id):
#         self.id = id
#         id = 2

# t = test(1)
# print(t.id)

# def a(b, c, d): pass

# a = 7
# print(a.__str__())

test = set ([1 ,2, 11]) == set ([1, 2])

print(test)

# Ordenar primeiro por comprimento, depois alfabeticamente
palavras = ["banana", "maçã", "uva", "laranja", "kiwi"]
palavras.sort(key=lambda x: (len(x), x))
print(palavras)  # ['uva', 'kiwi', 'maçã', 'banana', 'laranja']

# Ordenar por múltiplos critérios em dicionários
pessoas = [
    {"nome": "João", "idade": 25, "cidade": "SP"},
    {"nome": "Maria", "idade": 25, "cidade": "RJ"},
    {"nome": "Pedro", "idade": 30, "cidade": "SP"}
]

# Ordenar por idade (crescente) e depois por nome (crescente)
pessoas.sort(key=lambda x: (x["idade"], x["nome"]))
print([f"{p['nome']}-{p['idade']}" for p in pessoas])
# ['João-25', 'Maria-25', 'Pedro-30']