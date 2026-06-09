programa
{
	
	funcao inicio()
	{
		inteiro paes, qijo, bisn, paof, leit, paodoce, suspiro
		escreva("quantos pães deseja comprar?\n")
		leia (paes)
		escreva("quantos queijos deseja comprar?\n")
		leia (qijo)
		escreva("quantos bisnagas deseja comprar?\n")
		leia (bisn)
		escreva("quantos pão de forma deseja comprar?\n")
		leia (paof)
		escreva("quantos pães leite comprar?\n")
		leia (leit)
		escreva("quantos pães pão doce comprar?\n")
		leia (paodoce)
		escreva("quantos pães suspiro comprar?\n")
		leia (suspiro)

		real total = (paes * 1.00) + (qijo * 14.00) + (bisn * 6.00) + (paof * 10.00) + (leit * 8.50) + (paodoce * 6.00) + (suspiro * 6.00)

		se (paes == 10 e qijo >=1){
		escreva ("vc ganhou 10% de desconto!")
		} senao se (bisn >=  1 ou paof >= 1) {
			escreva ("vc ganhou 15% de desconto!") }
			senao se (leit >= 1 e paodoce >= 1 ou suspiro >= 1) {
				escreva ("vc ganhou 5% de desconto") }
				senao {
					escreva (" compra finalizada:", total) }
				}
		}
}