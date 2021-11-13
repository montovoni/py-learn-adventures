salario = float(input('Digite seu valor monétario R$:'))


salario_15_porcento = salario * 0.15
salario_10_porcento = salario * 0.10


if salario <= 1250:
    print('Com um aumento de 15%,seu salário atual sera de R${}'.format(salario_15_porcento+salario))
elif salario > 1250:
    print('Com um aumento de 15%,seu salário atual sera de R${}'.format(salario_10_porcento+salario))
else:
    print('Erro!')