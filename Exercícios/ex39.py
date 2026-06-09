pilotos = int(input("Quantidade de pilotos: "))

nome = input("Nome do piloto: ")
tempo = float(input("Velocidade/tempo da volta: "))

nome_mais_rapido = nome
nome_mais_lento = nome

melhor_tempo = tempo
pior_tempo = tempo

soma = tempo
contador = 1

while contador < pilotos:
    nome = input("Nome do piloto: ")
    tempo = float(input("Velocidade/tempo da volta: "))

    soma += tempo

    if tempo < melhor_tempo:
        melhor_tempo = tempo
        nome_mais_rapido = nome

    if tempo > pior_tempo:
        pior_tempo = tempo
        nome_mais_lento = nome

    contador += 1

media = soma / pilotos

print("\n===== RESULTADO FINAL =====")
print("Piloto mais rápido:", nome_mais_rapido)
print("Piloto mais lento:", nome_mais_lento)
print(f"Média das voltas: {media:.2f}")