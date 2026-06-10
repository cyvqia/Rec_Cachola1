pao = int(input("Quantos pães deseja comprar? \n"))
queijo = int(input("Quantos queijos deseja comprar? \n"))
bisnaga = int(input("Quantas bisnagas deseja comprar? \n"))
paodeforma = int(input("Quantos pão de forma deseja comprar? \n"))
leite = int(input("Quantos pães leite deseja comprar? \n"))
paodoce = int(input("Quantos pães pão doce deseja comprar? \n"))
suspiro = int(input("Quantos pães suspiro deseja comprar? \n"))
if pao == 10 and queijo >= 1:
	print("Você ganhou 10% de desconto!")
elif bisnaga >= 1 or paodeforma >= 1:
	print("Você ganhou 15% de desconto!")
elif leite >= 1 and paodoce >= 1 or suspiro >= 1:
	print("Você ganhou 5% de desconto!")
else:
	print("Compra finalizada.")