# list comprehension pra criar um tabuleiro de xadrez:
# [ ] - para posições vazias
# tor - para torre
# cav - para cavalo
# bis - para bispo
# rei - para rei
# rai - para rainha
# pão - para peão

# tabuleiro = [
#     ["[tor]", "[cav]", "[bis]", "[rei]", "[rai]", "[bis]", "[cav]", "[tor]"],
#     ["[pão]"] * 8,
#     ["[   ]"] * 8,
#     ["[   ]"] * 8,
#     ["[   ]"] * 8,
#     ["[   ]"] * 8,
#     ["[pão]"] * 8,
#     ["[tor]", "[cav]", "[bis]", "[rei]", "[rai]", "[bis]", "[cav]", "[tor]"]
# ]

# # for linha in tabuleiro:
# #     print(linha)

# tabuleiro2 = [["[   ]" for casa in range(8)] for linha in range(8)]
# linha_peoes = []*8
# for i in range(8):
#     linha_peoes.append("[peã]")
# tabuleiro2[1] = linha_peoes
# tabuleiro2[6] = linha_peoes.copy()
# tabuleiro2[0] = ["[tor]", "[cav]", "[bis]", "[rei]", "[rai]", "[bis]", "[cav]", "[tor]"]
# tabuleiro2[7] = ["[tor]", "[cav]", "[bis]", "[rei]", "[rai]", "[bis]", "[cav]", "[tor]"]

# def mostrar_tabuleiro():
#     """Mostra o tabuleiro no formato atual"""
#     for linha in tabuleiro2:
#         print(' '.join(linha))

# def mover_peca():
#     """Permite mover peças no tabuleiro"""
#     while True:
#         print("\nTabuleiro atual:")
#         mostrar_tabuleiro()
        
#         try:
#             # Obter coordenadas de origem
#             origem = input("\nDigite a linha e coluna de origem (ex: 1,2) ou 'sair': ")
#             if origem.lower() == 'sair':
#                 break
                
#             linha_orig, col_orig = map(int, origem.split(','))
            
#             # Verificar se há peça na origem
#             if tabuleiro2[linha_orig][col_orig] == "[   ]":
#                 print("Não há peça nesta posição!")
#                 continue
                
#             # Obter coordenadas de destino
#             destino = input("Digite a linha e coluna de destino (ex: 2,2): ")
#             linha_dest, col_dest = map(int, destino.split(','))
            
#             # Realizar movimento
#             peca = tabuleiro2[linha_orig][col_orig]
#             tabuleiro2[linha_dest][col_dest] = peca
#             tabuleiro2[linha_orig][col_orig] = "[   ]"
            
#             print(f"Peça movida de ({linha_orig},{col_orig}) para ({linha_dest},{col_dest})")
            
#         except (ValueError, IndexError):
#             print("Entrada inválida! Use o formato: número,número (ex: 1,2)")
#         except Exception as e:
#             print(f"Erro: {e}")

# # Para usar a função de movimento:
# mover_peca()

# def soma(num1, num2):
#     return num1 + num2

# def multiplica(num1, num2):
#     return num1 * num2

# def subtrai(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     if num2 == 0:
#         return "Erro: Divisão por zero não é permitida."
#     return num1 / num2

# operador = multiplica(soma(2, 3), subtrai(10, 4))
# print(operador)

def calcula(num1, num2,):
    soma = num1 + num2
    return num1, num2, soma

# resultado = calcula(2, 3)
# print(f"A soma de {resultado[0]} + {resultado[1]} é {resultado[2]}")

# Usando *args e **kwargs:

def soma(*nuns):
    resultado = 0
    for número in nuns:
        resultado += número
    return resultado

# print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def usuario(**dicios):
    for chave, valor in dicios.items():
        print(f"{chave.capitalize()}: {valor}")

# usuario(nome="Ana", idade=30, cidade="São Paulo", profissão="Engenheira")

# curiosidade sobre funções (def), para se enviar uma função como parâmetro de outra função, sem executá-la, basta não usar os parênteses.

def executa(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

# print(executa(soma, 1, 2, 3, 4, 5))
# print(executa(usuario, nome="Carlos", idade=25, cidade="Rio de Janeiro", profissão="Designer"))


