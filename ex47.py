onibus = []
numero = 1

for linha in range(6):
    nova = []
    for coluna in range(7):
        nova.append(numero)
        numero += 1
    onibus.append(nova)

while True:

    print("\nPOLTRONAS DISPONÍVEIS")
    print(onibus)
    lugar = int(input("\nDigite o lugar desejado (1-42): "))

    for i in range(6):
        for j in range(7):
            if onibus[i][j] == lugar:
                onibus[i][j] = "X"
                print("Lugar vendido!")
                break

            if onibus[i][j] == "X":
                print("Lugar já vendido.")

    op = input("Deseja comprar outro lugar? (Sim/Não): ")
    if op.lower() != "sim":
        print("Obrigado por comprar conosco!")
        break
