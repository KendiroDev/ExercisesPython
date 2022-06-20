nome = input ("Digite seu nome")
salario = float (input ("Digite seu salario fixo"))
vendasmes = float (input ("Digite o total de vendas no mês em dinheiro"))

salariodevendas = (vendasmes *15) / 100
salariofinal = (salario + salariodevendas)

print (" ")
print (nome, " Seu salario no final do mês foi de: ", salariofinal)

