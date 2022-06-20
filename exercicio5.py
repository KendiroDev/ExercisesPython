

sabao1 = float (input("digite o valor do sabão no dia 01/04"))
deter1 = float (input("digite o valor do detergente no dia 01/04"))
refri1 = float (input("digite o valor do refrigerante no dia 01/04"))

sabao2 = float (input("digite o valor do sabão no dia 01/05"))
deter2 = float (input("digite o valor do detergente no dia 01/05"))
refri2 = float (input("digite o valor do refrigerante no dia 01/05"))

infla1 = ((sabao2 * 100) / sabao1 ) - 100
dif1 = sabao2 - sabao1
infla2 = ((deter2 * 100) / deter1 ) - 100
dif2 =  deter2 - deter1
infla3 = ((refri2 * 100) / refri1 ) - 100
dif3 = refri2 - refri1

print ("o produto sabão teve uma inflação de ", infla1,"% uma diferença de preço de ", dif1"reais")
print ("o produto detergente teve uma inflação de ", infla2,"% uma diferença de preço de ", dif2"reais")
print ("o produto refrigerante teve uma inflação de ", infla3,"% uma diferença de preço de ", dif3"reais")

