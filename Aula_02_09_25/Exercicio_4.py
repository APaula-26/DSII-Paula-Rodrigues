# Faça um programa que solicite dois números ao usuário (com decimais). Em seguida solicite que o usuário informe o 
# Resultado das quatro operações matemáticas (subtração, multiplicação, soma, divisão)

n1 = float(input("Informe um número decimal:"))
n2 = float(input("Informe mais um número decimal:"))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
subtracao = n1 - n2

print("O resultado da soma é:",soma)
print("O resultado da subtração é:",subtracao)
print("O resultado da multiplicação é:", multiplicacao)
print("O resultado da divisão é:",divisao)