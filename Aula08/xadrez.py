tabuleiro2 = [["[   ]" for casa in range(8)] for linha in range(8)]

# Criar listas separadas para cada fileira de peões
linha_peoes_brancos = ["[P-b]" for i in range(8)]
linha_peoes_pretos = ["[P-p]" for i in range(8)]

tabuleiro2[1] = linha_peoes_pretos  # Peões pretos
tabuleiro2[6] = linha_peoes_brancos  # Peões brancos

tabuleiro2[0] = ["[T-p]", "[C-p]", "[B-p]", "[R-p]", "[Q-p]", "[B-p]", "[C-p]", "[T-p]"]  # Pretas
tabuleiro2[7] = ["[T-b]", "[C-b]", "[B-b]", "[R-b]", "[Q-b]", "[B-b]", "[C-b]", "[T-b]"]  # Brancas

def mostrar_tabuleiro():
    """Mostra o tabuleiro no formato atual"""
    print("    0     1     2     3     4     5     6     7")
    for i, linha in enumerate(tabuleiro2):
        print(f"{i} {' '.join(linha)} {i}")
    print("    0     1     2     3     4     5     6     7")

def obter_cor(peca):
    """Retorna a cor da peça ('b' para branco, 'p' para preto, None para vazio)"""
    if peca == "[   ]":
        return None
    return peca[-2]  # O penúltimo caractere indica a cor

def movimento_valido(linha_orig, col_orig, linha_dest, col_dest, jogador_atual):
    """Verifica se o movimento é válido para a peça"""
    peca = tabuleiro2[linha_orig][col_orig]
    cor_peca = obter_cor(peca)
    
    # Verificar se é a vez do jogador correto
    if (jogador_atual == "brancas" and cor_peca != "b") or (jogador_atual == "pretas" and cor_peca != "p"):
        return False, "Não é a vez deste jogador"
    
    # Verificar se há peça na origem
    if peca == "[   ]":
        return False, "Não há peça nesta posição"
    
    # Verificar se está tentando capturar própria peça
    peca_destino = tabuleiro2[linha_dest][col_dest]
    cor_destino = obter_cor(peca_destino)
    if cor_destino == cor_peca:
        return False, "Não pode capturar própria peça"
    
    # Verificar movimento específico para cada tipo de peça
    tipo_peca = peca[1]  # O segundo caractere indica o tipo da peça
    
    # Movimento do Peão
    if tipo_peca == "P":
        direcao = -1 if cor_peca == "b" else 1  # Brancos sobem (linha diminui), pretos descem (linha aumenta)
        
        # Movimento para frente
        if col_orig == col_dest and peca_destino == "[   ]":
            # Movimento normal (1 casa)
            if linha_dest == linha_orig + direcao:
                return True, ""
            # Movimento inicial (2 casas)
            if (linha_orig == 6 and cor_peca == "b" and linha_dest == 4 and 
                tabuleiro2[5][col_orig] == "[   ]") or \
               (linha_orig == 1 and cor_peca == "p" and linha_dest == 3 and 
                tabuleiro2[2][col_orig] == "[   ]"):
                return True, ""
        
        # Captura diagonal
        if abs(col_dest - col_orig) == 1 and linha_dest == linha_orig + direcao and peca_destino != "[   ]":
            return True, ""
        
        return False, "Movimento inválido para o peão"
    
    # Movimento da Torre
    elif tipo_peca == "T":
        # Torre move na mesma linha ou mesma coluna
        if linha_orig != linha_dest and col_orig != col_dest:
            return False, "Torre só pode mover na horizontal ou vertical"
        
        # Verificar se há peças no caminho
        if linha_orig == linha_dest:  # Movimento horizontal
            inicio = min(col_orig, col_dest) + 1
            fim = max(col_orig, col_dest)
            for col in range(inicio, fim):
                if tabuleiro2[linha_orig][col] != "[   ]":
                    return False, "Há peças no caminho"
        else:  # Movimento vertical
            inicio = min(linha_orig, linha_dest) + 1
            fim = max(linha_orig, linha_dest)
            for linha in range(inicio, fim):
                if tabuleiro2[linha][col_orig] != "[   ]":
                    return False, "Há peças no caminho"
        
        return True, ""
    
    # Movimento do Cavalo
    elif tipo_peca == "C":
        # Cavalo move em L (2 casas em uma direção e 1 na perpendicular)
        dif_linha = abs(linha_dest - linha_orig)
        dif_col = abs(col_dest - col_orig)
        if not ((dif_linha == 2 and dif_col == 1) or (dif_linha == 1 and dif_col == 2)):
            return False, "Movimento inválido para o cavalo"
        return True, ""
    
    # Movimento do Bispo
    elif tipo_peca == "B":
        # Bispo move na diagonal
        if abs(linha_dest - linha_orig) != abs(col_dest - col_orig):
            return False, "Bispo só pode mover na diagonal"
        
        # Verificar se há peças no caminho
        passo_linha = 1 if linha_dest > linha_orig else -1
        passo_col = 1 if col_dest > col_orig else -1
        
        linha_atual, col_atual = linha_orig + passo_linha, col_orig + passo_col
        while linha_atual != linha_dest and col_atual != col_dest:
            if tabuleiro2[linha_atual][col_atual] != "[   ]":
                return False, "Há peças no caminho"
            linha_atual += passo_linha
            col_atual += passo_col
        
        return True, ""
    
    # Movimento da Rainha
    elif tipo_peca == "Q":
        # Rainha move como torre + bispo
        mesma_linha = linha_orig == linha_dest
        mesma_coluna = col_orig == col_dest
        mesma_diagonal = abs(linha_dest - linha_orig) == abs(col_dest - col_orig)
        
        if not (mesma_linha or mesma_coluna or mesma_diagonal):
            return False, "Movimento inválido para a rainha"
        
        # Verificar se há peças no caminho
        if mesma_linha:  # Movimento horizontal
            inicio = min(col_orig, col_dest) + 1
            fim = max(col_orig, col_dest)
            for col in range(inicio, fim):
                if tabuleiro2[linha_orig][col] != "[   ]":
                    return False, "Há peças no caminho"
        elif mesma_coluna:  # Movimento vertical
            inicio = min(linha_orig, linha_dest) + 1
            fim = max(linha_orig, linha_dest)
            for linha in range(inicio, fim):
                if tabuleiro2[linha][col_orig] != "[   ]":
                    return False, "Há peças no caminho"
        else:  # Movimento diagonal
            passo_linha = 1 if linha_dest > linha_orig else -1
            passo_col = 1 if col_dest > col_orig else -1
            
            linha_atual, col_atual = linha_orig + passo_linha, col_orig + passo_col
            while linha_atual != linha_dest and col_atual != col_dest:
                if tabuleiro2[linha_atual][col_atual] != "[   ]":
                    return False, "Há peças no caminho"
                linha_atual += passo_linha
                col_atual += passo_col
        
        return True, ""
    
    # Movimento do Rei
    elif tipo_peca == "R":
        # Rei move uma casa em qualquer direção
        if abs(linha_dest - linha_orig) > 1 or abs(col_dest - col_orig) > 1:
            return False, "Rei só pode mover uma casa em qualquer direção"
        return True, ""
    
    return False, "Tipo de peça desconhecido"

def mover_peca():
    """Permite mover peças no tabuleiro com controle de turnos"""
    jogador_atual = "brancas"  # Começa com as brancas
    
    while True:
        print(f"\nVez das {jogador_atual.upper()}")
        mostrar_tabuleiro()
        
        try:
            # Obter coordenadas de origem
            origem = input("\nDigite a linha e coluna de origem (ex: 1,2) ou 'sair': ")
            if origem.lower() == 'sair':
                break
                
            linha_orig, col_orig = map(int, origem.split(','))
            
            # Obter coordenadas de destino
            destino = input("Digite a linha e coluna de destino (ex: 2,2): ")
            linha_dest, col_dest = map(int, destino.split(','))
            
            # Verificar se o movimento é válido
            valido, mensagem = movimento_valido(linha_orig, col_orig, linha_dest, col_dest, jogador_atual)
            
            if not valido:
                print(f"Movimento inválido: {mensagem}")
                continue
            
            # Realizar movimento
            peca = tabuleiro2[linha_orig][col_orig]
            tabuleiro2[linha_dest][col_dest] = peca
            tabuleiro2[linha_orig][col_orig] = "[   ]"
            
            print(f"Peça movida de ({linha_orig},{col_orig}) para ({linha_dest},{col_dest})")
            
            # Alternar jogador
            jogador_atual = "pretas" if jogador_atual == "brancas" else "brancas"
            
        except (ValueError, IndexError):
            print("Entrada inválida! Use o formato: número,número (ex: 1,2)")
        except Exception as e:
            print(f"Erro: {e}")

# Para usar a função de movimento:
mover_peca()