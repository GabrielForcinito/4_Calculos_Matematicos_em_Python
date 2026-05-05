import math
print("\nCálculo do volume do tronco de uma pirâmide")

# O tronco da pirâmide é o corpo da pirâmide sem sua ponta (Como se a ponta fosse cortada)
h = float(input("Digite o valor da altura do tronco da pirâmide: "))
bmaior = float(input("Digite o valor da base maior da pirâmide: "))
bmenor = float(input("Digite o valor da base menor da pirâmide: "))

volume = (h/3*(bmaior**2 + bmenor**2 + (math.sqrt(bmaior**2 * bmenor**2))))

print("\nO valor do volume do tronco da pirâmide é de %.2f m³\n" % (volume))