cont = 0

while cont < 5:
    num_bolinhas = int(input("Quantas bolinhas de gude tem no pode de vidro? "))

    if num_bolinhas == 82:
        print("Parabéns, você acertou!")
    elif num_bolinhas < 82:
        print("Você errou! Existem mais bolinhas do que você digitou.")
    elif num_bolinhas > 82:
        print("Você errou! Existem menos bolinhas do que você digitou.")
    cont = cont + 1

else:
    print("Acabou suas chances!")
