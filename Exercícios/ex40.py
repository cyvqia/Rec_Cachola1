cont = 0
erros_abaixo = 0
erros_acima = 0

oportunidades = int(input("Quantas oportunidades deseja ter? "))

while cont < oportunidades:
    num_bolinhas = int(input("Quantas bolinhas de gude tem no pote de vidro?: "))

    if num_bolinhas == 82:
        print("Parabéns, você acertou!")
    elif num_bolinhas < 82:
        print("Você errou! Existem mais bolinhas do que você digitou.")
        erros_abaixo += 1
    elif num_bolinhas > 82:
        print("Você errou! Existem menos bolinhas do que você digitou.")
        erros_acima += 1

    cont += 1

    continuar = input("Deseja continuar? (s/n): ").lower()

    if continuar != "s":
        break

print("\n===== RELATÓRIO =====")
print("Tentativas realizadas:", cont)

if erros_abaixo > erros_acima:
    print("Erro mais comum: números abaixo do valor correto.")
elif erros_acima > erros_abaixo:
    print("Erro mais comum: números acima do valor correto.")
else:
    print("Os erros acima e abaixo ocorreram na mesma quantidade.")
