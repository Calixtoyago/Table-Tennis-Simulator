import random
from atletas import atletas

def alternar_saque(deuce, cont_saque, jogadores, sacar, receber):
    if deuce:
        sacar, receber = (jogadores[1], jogadores[0]) if sacar == jogadores[0] else (jogadores[0], jogadores[1])
        cont_saque = 0
    elif cont_saque == 2:
        sacar, receber = (jogadores[1], jogadores[0]) if sacar == jogadores[0] else (jogadores[0], jogadores[1])
        cont_saque = 0

    return sacar, receber, cont_saque

def Partida(j1, j2):
    games = {}

    game_j1, game_j2 = 0, 0
    pontos_j1 = 0
    pontos_j2 = 0

    game = 1

    jogadores = [j1, j2]
    random.shuffle(jogadores)
    sacar, receber = jogadores
    cont_saque = 0

    PESO_ATAQUE = 1.3
    PESO_DEFESA = 1.1
    VARICACAO = 8
    ERRO_BASE = 0.05

    while game_j1 < 3 and game_j2 < 3:
        deuce = False
        while True:
            
            print(f'Saque: {sacar.nome}')

            chance_erro = (10 - sacar.saque) / 10
            chance_ace = (sacar.saque / (sacar.saque + receber.defesa)) * 0.15

            if random.random() < chance_erro: # errou o saque
                if sacar == j1:
                    pontos_j2 += 1
                else:
                    pontos_j1 += 1
                print('Errou o saque')
            elif random.random() < chance_ace: # fez um ace
                if sacar == j1:
                    pontos_j1 += 1
                else:
                    pontos_j2 += 1
                print('Fez Ace')
            else: # continua o jogo
                random.shuffle(jogadores) #aleatorizar o jogador a atacar

                jogador_ataque, jogador_defesa = jogadores

                ataque = jogador_ataque.ataque * PESO_ATAQUE + random.randint(0, VARICACAO)
                defesa = jogador_defesa.defesa * PESO_DEFESA + random.randint(0, VARICACAO)

                chance_ataque = ataque / (ataque + defesa)

                if random.random() < ERRO_BASE:
                    vencedor = jogador_defesa
                else:
                    vencedor = jogador_ataque if random.random() < chance_ataque else jogador_defesa

                if vencedor == j1:
                    pontos_j1 += 1
                else:
                    pontos_j2 += 1

                if pontos_j1 == 10 and pontos_j2 == 10:
                    deuce = True # quando os sets passam a ser vencidos com a diferenca de 2
                    # vai ser usado para mudar a alternancia dos saques para 1 ponto
                    print('-- DEUCE --')

            cont_saque += 1 #contador dos pontos para alternancia dos saques

            sacar, receber, cont_saque = alternar_saque(deuce, cont_saque, jogadores, sacar, receber)

            if pontos_j1 >= 11 and pontos_j1 - pontos_j2 >= 2:
                game_j1 += 1
                break

            if pontos_j2 >= 11 and pontos_j2 - pontos_j1 >= 2:
                game_j2 += 1
                break
        print('Fim do game')

        games[game] = (pontos_j1, pontos_j2)
        pontos_j1 = 0
        pontos_j2 = 0
        game += 1
    
    if game_j1 > game_j2:
        print(f'{j1.nome} GANHOU')
    else:
        print(f'{j2.nome} GANHOU')

    for games_finished, sets in games.items():
        print(f"{games_finished}: {sets}")

    return j1.nome if game_j1 > game_j2 else j2.nome

Partida(atletas[0], atletas[1])
