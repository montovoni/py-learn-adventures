import math

n1 = float(input("Cateto oposto: "))
n2 = float(input("Cateto adjacente: "))

hipotenusa = math.hypot(n1, n2)

print("\nA hipotenusa do seu triângulo retangulo é = {:.2f}".format(hipotenusa))