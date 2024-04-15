# Faça duas variáveis numéricas e descubra qual é a maior!
number01 = int(input('Digite um número: '))
number02 = int(input('Digite outro número: '))

if number01 > number02:
    print(f'O número {number01} é maior que o número {number02}')
    
elif number02 > number01: 
    print(f'O número {number02} é maior que o número {number01}') 
       
else:
    print(f'Os números {number01} e {number02} são iguais!')
