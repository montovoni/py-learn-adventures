import random

n1 = input("1° Aluno: ")
n2 = input("3° Aluno: ")
n3 = input("3° Aluno: ")
n4 = input("4° Aluno: ")

lista = [n1, n2, n3, n4]

print("\nO aluno sorteado sera: {}".format(random.choice(lista)))
