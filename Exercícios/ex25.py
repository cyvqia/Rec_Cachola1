25-
programa
{
	
	funcao inicio()
	{
		real peso, altura, imc
		escreva("digite seu peso\n")
		leia (peso)
		escreva("digite sua altura\n")
		leia (altura)
		imc = peso / (altura * altura)
		
		se (imc <18.5) {
			escreva("magraza") }
			senao se (imc >=18.5 e imc < 24.9) {			
				escreva("normal")}
				senao se (imc >=24.9 e imc <= 30) {
					escreva("sobre peso") }
					senao {
						escreva("obesidade") }
		}
}
