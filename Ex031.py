distancia = float(input('Qual a distância percorrida na viagem(KM): '))

if distancia <= 200:
    print("Você ira pagar R${} reais,pois rodou {}KM".format(distancia*0.50, distancia))
elif distancia > 200:
    print("Você ira pagar R${} reais,pois rodou {}KM".format(distancia*0.45, distancia))