idade = int(input("Informe sua idade: "))
print("1 - Carteira B")
print("2 - Carteira C")
op = int(input("Informe seu tipo de carteira: "))
if op == 1:
    print("Está habilidado por pelo menos 2 anos?")
    res = input("[S/N]: ")
elif op == 2:
    print("Está habilidado por pelo menos 1 ano?")
    res = input("[S/N]: ")
    
print("Cometeu alguma infração nos últimos 12 meses?")
res2 = input("[S/N]: ")
    
if (idade >= 21 and res == "S" and res2 == "N"):
    print("Está apto.")
    print("Está apto.")
else:
    print("Não está apto.")
