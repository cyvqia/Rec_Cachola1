total = 0
num = 0
cont =0

while True:
    num = int(input("Digite um número: "))

    if num <= 0:
        print("Número negativo, tente novamente!")
        continue
    
    total = total + num
    cont = cont + 1
    print (cont)
    
    if total >= 100:
        print (f"Resultado da soma: {total}")
        print (f"Tentativas feitas: {cont}")
        break