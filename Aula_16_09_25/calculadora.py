# Elaborar um algoritmo 'Calculadora' utilizando todos os recursos e comando ensinados em sala de aula
# Soma, Divisão, Multiplicação, Subtração

print("\n Olá, você está na Calculadora da Ana Paula Rodrigues!!")
print('  \n              Menu                ')
operacao=(input("Informe a operação matematica desejada: \n 1-Soma \n 2-Subtração \n 3-Multiplicação  \n 4-Divisão \n 5-Exponênciação \n 6- Raiz Quadrada \n Digite a sua escolha:  "))
num1 = float(input("  Digite um número:"))
num2 = float(input("  Digite outro número:"))


Soma = num1 + num2
Subtracao = num1 - num2
Multiplicacao = num1 * num2
Divisao = num1 / num2 if num2 !=0 else "ERRO - Divisão por zero não permitida"
Exponenciacao = num1 ** num2
raiz = num1**0.5 

if operacao == "1":
    print ("  O resultado da sua Soma é:",Soma)
elif operacao == "2":
    print("   O resultado da sua Subtração é:",Subtracao)
elif operacao == "3":
    print("   O resultado da sua Multiplicação é:",Multiplicacao)
elif operacao == "4":
    print("   O resultado da sua Divisão é:",Divisao)
elif operacao == "5":
    print("   O resultado da exponenciação é:",Exponenciacao)
elif operacao == "6":
    print("A raiz de",num1,"é",raiz)
else:
    print("   Insira uma operação valida")
