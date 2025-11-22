# Faça um algoritmo que receba um valor de uma compra e receba o numero de prestações, apresente o valor das
# prestações sem juros. 

Vc = float(input("Informe o valor da compra:"))
Qp = int(input("Informe a quantidade de prestações:"))

print("O valor das prestações sem juros ficam em: R$",Vc/Qp)