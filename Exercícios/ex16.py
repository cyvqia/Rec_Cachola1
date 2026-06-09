nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6.0:
    print("APROVADO")
elif media <6.0:
    print("EM RECUPERAÇÃO")
    print(media)
    if media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
else:
    print("REPROVADO")