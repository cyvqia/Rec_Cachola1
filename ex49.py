
def vogal(letra):
    vogal = ["a", "e", "i", "o", "u"]
    if letra in vogal:
        print("É uma vogal.")
    else:
        print("É uma consoante.")

while True:
    letra = input("Informe uma letra: ")
    vogal(letra)
    opcao = input("Deseja continuar? (s/n): ")
    if opcao.lower() == "n":
        break
