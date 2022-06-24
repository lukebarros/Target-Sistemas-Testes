v1 = 110
v2 = 80
S = 100

#Quando os dois automoveis se encontram temos:
t = S/(v1 + v2)
tb = t + 10/60 #tempo de pedágio do caminhão

#Calculo da distância dos automoveis para as cidades
delta = S - (v2 * tb)

print("O Carro está a %.2f km de Ribeirão Preto <-> Franca" % (S - delta))
print("O Caminhão está a %.2f km de Franca <-> Ribeirão Preto" % delta)
print("O mais próximo será o Caminhão")