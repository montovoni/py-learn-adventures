bissexto = int(input('Digite um ano: '))

if bissexto % 400 == 0 or bissexto % 4 == 0:
    print("È BISSEXTO")
else:
    print('Não é BISSEXTO')