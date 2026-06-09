valor_suco1 = 5.50
quant_suco = int(input("Informe a quantia de sucos comprados: "))

if quant_suco > 10:
    valor_suco2 = 4.50
    soma1 = 4.50 * quant_suco
    res1 = soma1
    print("A quantidade de sucos desejados é:", quant_suco, "e o valor a ser pago é:", res1)
else:
    soma2 = 5.50 * quant_suco
    res2 = soma2
    print("A quantidade de sucos desejados é:", quant_suco, "e o valor a ser pago é:", res2)