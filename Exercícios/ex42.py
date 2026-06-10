while True:
    dia = int(input("Digite o dia que deseja pagar o boleto: "))

    if dia == 2 or dia == 5 or dia == 10:
        print("Dia disponível registrado.")
        break
    else:
        print(f"O dia {dia} não está disponível.")