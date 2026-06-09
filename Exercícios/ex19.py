programa 
{  	 
 	funcao inicio()  	{ 
 	 	real gasolina, etanol, total  	 	 
 	 	escreva ("digite o preço da gasolina:")  	 	leia (gasolina) 
 	 	escreva ("digite o preço do etanol:")  	 	leia (etanol) 
 	 	total = gasolina / etanol 
 
 	 	se (total >= 0.7) { 
 	 	escreva ("compensa abastecer com gasolina") } 
 	 	senao { 
 	 	 	escreva ("compensa abastecer com etanol") 
 	 	}  	} 
} 
