senha = []

for linha in range (6):
    valor = input("Digite a senha (em minúsculo): ")
    if valor in["a", "e", "i", "o", "u"]:
        senha.append(valor)
    else:
        print("Digito inválido, tente novamente.")
        continue

nova_senha = []

for i in range (len(senha)):
    if senha [i] == "a":
        nova_senha.append("z")
    elif senha [i] == "e":
        nova_senha.append("3")
    elif senha [i] == "i":
        nova_senha.append("L")
    elif senha [i] == "o":
        nova_senha.append("0")
    elif senha [i] == "u":
        nova_senha.append("$")

print(f"Senha: {senha}")
print(f"Senha criptografada: {nova_senha}")
