# import dis

# def minha_funcao(x, y):
#     return x * y + 10

# # Desmonta o bytecode para entender a execução
# dis.dis(minha_funcao)
# # Output mostra as instruções bytecode

# import inspect

# def exemplo(a, b=5):
#     """Função de exemplo"""
#     return a + b

# # Analisa a função
# print(inspect.getsource(exemplo))  # Mostra o código fonte
# print(inspect.signature(exemplo))  # Mostra a assinatura
# print(inspect.getmembers(exemplo)) # Lista membros e atributos

# import numpy as np

# # Inspeciona funções de bibliotecas
# print(dir(np.array))      # Lista métodos disponíveis
# print(help(np.dot))       # Mostra documentação

# Código antigo
def calc(a,b,c):
    x = a*b
    y = x+c
    return y

# Código reengenheirado
def calcular_produto_soma(multiplicando, multiplicador, soma):
    """
    Calcula: (multiplicando × multiplicador) + soma
    """
    produto = multiplicando * multiplicador
    resultado_final = produto + soma
    return resultado_final