largura = float(input('qual a largura da parede? '))
altura = float(input('qual a altura da parede? '))
area = largura*altura
print('a sua parede de altura {:.2f}m e largura {:.2f}m, tem de área total {:.2f}m2\ne vai precisar de {:.2f}l de tinta.'.format(altura, largura, area, area/2))
