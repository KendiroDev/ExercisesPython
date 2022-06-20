custfabrica = float (input("Digite o valor de custo de fabrica do carro: "))
custimposto = (custfabrica * 45) / 100
custimpostofinal = (custfabrica + custimposto)
custrevendedora = (custimpostofinal * 25) / 100
custrevendedorafinal = (custimpostofinal + custrevendedora)

print ("O custo final de fábrica do carro sairá em um valor de: ",custfabrica)
print ("O custo final do carro da fabrica + imposto saira em um valor de: ",custimpostofinal)
print ("O custo final do carro na revendedora sairá de: ",custrevendedorafinal)
print (" ")
print ("Abaixo o Valor de imposto e valor da revenderora")
print ("IMPOSTO = ",custimposto)
print("REVENDORA = ", custrevendedora)
