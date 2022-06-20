nome = input ("Digite o nome do funcionário: ")
salariofixo = float (input("Digite seu salario fixo: "))
carrosvendidos = int (input("Digite o número de carros vendidos: "))
precocarros = float (input("Digite o preço total de carros vendidos neste mês"))
comissao = (carrosvendidos * 50) + (precocarros * 0.95)

print(" ")
print (nome, "Seu salario no fim do mes será de ",comissao)