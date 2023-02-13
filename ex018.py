import math
ang = float(input('Digite um angulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('SENO = {:.2f}.\nCOSSENO = {:.2f}.\nTANGENTE = {:.2f}.'.format(sen , cos, tan))

'''
math.radians() - > converte para radianos
math.sin() / math.cos() / math.tan() -> calcula o seno, cosseno, tangente
respectivamente com um angulo como parametro
