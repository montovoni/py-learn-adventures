carro = int(input('Qual foi sua velocidade(KM): '))

if carro <= 80:
    print("Você não foi mutado")
elif carro > 80:
    print('Você foi multado,ira ter que pagar uma multa no valor de {}R$'.format((carro - 80)*7))
else:
    print('Você digitou algo errado')