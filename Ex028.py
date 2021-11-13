import random

pensamento_computador = random.randint(0,5)
pensamento_jogador = int(input('Escolha um número entre [0] e [5]: '))


if pensamento_jogador == pensamento_computador:
    print("ACERTOU! ele escolheu o número -> {}".format(pensamento_jogador))
else:
    print('Errou! tente novamente,o número sorteado foi {}'.format(pensamento_computador))

