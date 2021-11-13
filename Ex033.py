primeiro_numero = int(input('\033[92mDigite um número inteiro: '))
segundo_numero = int(input('Digite um número inteiro: '))
terceiro_numero = int(input('Digite um número inteiro: \033[m'))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print('\033[31mO número maior é {}\033[m'.format(primeiro_numero))
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print('\033[31mO número maior é {}\033[m'.format(segundo_numero))
elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    print('\033[31mO número maior é {}\033[m'.format(terceiro_numero))
else:
    print("\033[31m >>>> Ocorreu algum erro inesperado <<<<\033[m")


if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero:
    print('\033[31mO número menor é {}\033[m'.format(primeiro_numero))
elif segundo_numero < primeiro_numero and segundo_numero < terceiro_numero:
    print('\033[31mO número menor é {}\033[m'.format(segundo_numero))
elif terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero:
    print('\033[31mO número menor é {}\033[m'.format(terceiro_numero))
else:
    print('\033[31m>>>> Algo errado acontêceu <<<<.\033[m')

print('CORRETO?')