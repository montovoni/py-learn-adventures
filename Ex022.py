nome = input("Digite seu nome completo: ")

dividido = nome.split()

print("\nMaísculo: {}".format(nome.upper()))
print("Minusculo: {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(len(dividido[0])))
