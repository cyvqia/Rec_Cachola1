programa 
{  	 
    funcao inicio()  	{ 
        cadeia moeda  	 	inteiro qnt_moeda  	 	real valor_moeda, total 
        escreva("digite uma moeda (ex dolar,real):") 
        leia (moeda) 
        escreva ("digite a quantidade dessa moeda:")  	 	leia (qnt_moeda) 
        escreva("digite quanto vale essa moeda:") 
 	 	leia (valor_moeda)  	 	total = (qnt_moeda * valor_moeda) 
        escreva("moeda escolhida: ", moeda, ",quantidade: ", qnt_moeda, 
",Valor atual da moeda: ",valor_moeda, "\ntotal:", total) 
	}
}