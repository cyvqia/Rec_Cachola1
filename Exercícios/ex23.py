programa
{
	
	funcao inicio()
	{
		cadeia op
		escreva("----menu de sucos----")
		escreva("\n L- Suco de Laranja")
		escreva("\n M- Suco de Morango")
		escreva("\n A- Suco de Acerola")
		escreva("\n
 U- Suco de Uva\n")
		leia(op)

		se (op == "L") {
			escreva ("Esse suco obtem vitaminas C!") }
			senao se (op == "M") {
				escreva ("Esse suco obtem vitaminas A!") }
				senao se (op == "A") {
					escreva ("Esse suco obtem vitaminas C!") }
					senao {
						escreva ("Esse suco obtem vitaminas E!") }
		}
}
