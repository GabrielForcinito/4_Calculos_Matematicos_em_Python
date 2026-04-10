print("\nCálculo para Prestação em Atraso ")

valprest = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem de atraso da multa: "))
qtddias = int(input("Digite quantos dias de atraso está: "))

prestacao = (valprest + (valprest*(multa/100)*qtddias))

print(f"\nO valor total da prestação com multa é R${prestacao: .2f}\n")