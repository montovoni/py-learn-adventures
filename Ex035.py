reta_1 = int(input('\033[92mDigite a primeira reta:'))
reta_2 = int(input('Digite a segunda reta:'))
reta_3 = int(input('Digite a terceira reta:\033[m'))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print('\033[33mOs 3 lados formam um triângulo\033[m')
else:
    print('\033[33mErro\033[m')