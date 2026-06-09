programa
{
	
	funcao inicio()
	{
		cadeia op
		
		escreva("digite uma estação do mês: \n")
		leia (op)

		se (op == "outono") {
			escreva("outono é 20 de março") }
			senao se (op == "inverno") {
				escreva("inverno é 21 de junho") }
			senao se (op == "primavera") {
				escreva("primavera é 22 de setembro") }
				senao {
					escreva("verão é 21 de dezembro")}
		}
}
