total = 0
n = 0
cont = 0

while True:
    n = int(input("digite um numero: "))
    total = total + n
    cont = cont + 1
    print (cont)
    
    if total >= 100:
        print (f"resultado da soma: {total}")
        print (f"tentativas feitas: {cont}")
        break