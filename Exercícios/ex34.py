cont = 0
alto = 0

while cont < 12:
    altura = float(input("Digite a altura do atleta: "))

    if altura >= 1.90:
        alto = alto + 1

    cont = cont + 1

print("De 12 atletas, os que tem altura igual a 1.90m ou mais é:", alto)
