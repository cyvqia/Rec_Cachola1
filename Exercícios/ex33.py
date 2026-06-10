total = 0
cont = 0
maior = 0

while cont < 10:
    num = int(input("Digite um número: "))

    if num > maior:
        maior = num

    total = total + num

    cont = cont + 1

print("de 10 numeros lidos, o maior é:", maior)
print("O total é:", total)
