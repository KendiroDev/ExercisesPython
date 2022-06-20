relatorio = 0
nprestacoes = 0

def valorpagamento (prestacao, atraso, valorfinal):
    prestacao = float(input('Qual o valor da prestação?: R$'))
    atraso = int(input('Quantos dias há de atraso do pagamento?: '))
    if atraso > 0:
        valorfinal = ((((atraso * 0.001) + 0.03) + 1) * prestacao)
        global relatorio
        global nprestacoes
        relatorio = relatorio + valorfinal
        nprestacoes += 1
        print('O valor da prestação é de: R${:.2f}'.format(prestacao))
        print('Foram {:02d} dias sem pagar, juros a 3% do valor + 0,1% pra cada dia'.format(atraso))
        print('Valor final a se pagar é o total de: R${:.2f}'.format(valorfinal))

    else:
        valorfinal = prestacao
        relatorio = relatorio + valorfinal
        nprestacoes += 1
        print('O valor da prestação é de: R${:.2f}'.format(prestacao))
        print('Foram {:02d} dias sem pagar, sem juros a se pagar'.format(atraso))
        print('Valor final a se pagar é o total de: R${:.2f}'.format(valorfinal))

contador = 0
while contador != 3:
    print(' ')
    print('*'*35)
    print('*            PRESTAÇÕES           *')
    print('*     1- Calcular prestações      *')
    print('*     2- Relatorio do dia         *')
    print('*     3- Sair                     *')
    print('*                                 *')
    print('*'*35)
    print(' ')
    print(' ')
    contador = int(input('Selecione uma das opções acima: '))
    print(' ')
    print(' ')
    if contador == 1:
        valorpagamento(prestacao=0, atraso=0, valorfinal=0)
    elif contador == 2:
        print('----- Foram pagas o total de {} prestações no dia de hoje !!!!! --------'.format(nprestacoes))   
        print('----- A somatoria de todas as prestações ficou no valor de R${:.2f} ----'.format(relatorio))
        print(' ')
        

    else:
        print(' ')
        print(' ')
        print('Programa encerrado!!!!!!')
        print(' ')
        print(' ')
        break
