#faça um programa que leia algo pelo teclado e na tela o  seu tipo primitivo e todas as informações possivel sobre ele.
msg = input('digite qualquer coisa: ')
print('Seu tipo primitivo é',type(msg))
print('maiusculo?:',msg.isupper())
print('é alfabetico?:',msg.isalpha())
print('é alfa-numerico?:',msg.isalnum())
print('é numérico:?',msg.isnumeric())
print('é numero decimal?:', msg.isdecimal())
print('é somente espaços?:', msg.isspace())
print('é minusculo?:', msg.islower())
print('é capitalizado?:', msg.istitle())