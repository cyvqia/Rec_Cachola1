pilotos = int(input("Quantidade de pilotos: "))

nome = input("Nome do piloto: ")
tempo = float(input("Velocidade/tempo da volta: "))

nome_rapido = nome
nome_lento = nome

melhor_tempo = tempo
pior_tempo = tempo

soma = tempo
cont = 1

while cont < pilotos:
    nome = input("Nome do piloto: ")
    tempo = float(input("Velocidade/tempo da volta: "))

    soma += tempo

    if tempo < melhor_tempo:
        melhor_tempo = tempo
        nome_rapido = nome

    if tempo > pior_tempo:
        pior_tempo = tempo
        nome_lento = nome

    cont += 1

media = soma / pilotos

print("\n===== RESULTADO FINAL =====")
print("Piloto mais rápido:", nome_rapido)
print("Piloto mais lento:", nome_lento)
print(f"Média das voltas: {media:.2f}")