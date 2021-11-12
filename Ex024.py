print("\nVamos verificar se sua cidade começa com SANTOS")
cidade = input("Escreva o nome da sua cidade: ").upper().strip()

frase = cidade.split()
frase2 = frase[0]

if frase2 == "SANTOS":
    print("VERDADEIRO")
else:
    print("FALSO")

