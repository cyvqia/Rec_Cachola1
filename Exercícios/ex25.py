peso = float(input("Digite seu peso: \n"))
altura = float(input("Digite sua altura: \n"))
imc = peso / (altura * altura)
if imc < 18.5:
	print("Magreza")
elif imc >= 18.5 and imc < 24.9:
	print("Normal")
elif imc >= 24.9 and imc <= 30:
	print("Sobrepeso")
else:
	print("Obesidade")