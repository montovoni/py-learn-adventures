frase = input("Digite uma frase: ").strip().upper()
print("Apareceram a letra A -{}- vezes".format(frase.count("A")))
print("Ela aparece primeira vez na posição: {}".format(frase.find("A")))
print("Ela aparece a última vez na posição: {}".format(frase.rfind("A")))