import math
num = float(input('Digite um n�mero fracionado: '))
print('o numero digitado {} tem sua parte inteira {}.'.format(num, math.trunc(num)))

# import math -> vai importar todo o m�dulo math e suas funcionalidades.
# para usa-lo use math.nome (nome da funcionalidade

# from math import nome (nome da funcionalidade) -> assim, nao
# importamos todas as funcionalidades, apenas a que desejamos usar
# naquele programa. desse modo nao se chama a funcao math. e s� a sua
# funcionalidade. trunc(num)

#math.ceil() -> arrendondad um numero fracionado para cima
#math.floor() -> arredonda um num fracionado para baixo
#math.trunc() -> mostra a parte inteira de um numero fracionado
