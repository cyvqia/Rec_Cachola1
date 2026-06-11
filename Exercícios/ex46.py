res_Final = []

for linha in range(11):
    nome = input("Digite o nome do jogador: ")
    gols = int(input("Digite a quantidade de gols: "))

    res_Final.append([nome, gols])

melhor_jogador = res_Final[0]

for jogador in res_Final:
    if jogador[1] > melhor_jogador[1]:
        melhor_jogador = jogador

print(f"O jogador {melhor_jogador[0]} é o melhor artilheiro com {melhor_jogador[1]} gols.")