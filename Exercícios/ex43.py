matriz = []

for linha in range (6):
    nova = []
    valor = float(input("Digite as velocidades dos pilotos: "))
    nova.append(valor)
    matriz.append(nova)
    
print("As velocidades são:")
for i in range (len(matriz) -1, -1, -1):
    print (matriz[i])