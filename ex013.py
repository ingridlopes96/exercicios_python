qtdDias = int(input('quantos dias voce ficou com o carro?: '))
qtdKm = float(input('quantos km voce rodou com o carro?: '))
custDia = 60*qtdDias
custKm = 0.15*qtdKm
print('voce alugou o carro por {} dias e rodou {}km.\nO preço a ser pago é: R${:.2f}'.format(qtdDias, qtdKm, custDia+custKm))
