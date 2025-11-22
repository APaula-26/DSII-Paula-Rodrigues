# Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor. 

num1 = int(input('Digite o 1º número:'))
num2 = int(input('Digite o 2º número:'))
if num1 > num2:
    print('O número',num1,'é maior que o número',num2)
elif num2 > num1:
    print('O número',num2,'é maior que o número',num1)
else:
    print('Os números digitados são equivalentes')

    # Correção do professor:
    # n1 = int(input('Informe um número:'))
    # n2 = int(input('Informe um número:'))
    # if n1 > n2:
    # print(f'O número {n1} é maior que o número {n2}')
    # else:
    # print(f'O número {n2} é maior que o número {n3}')

    # Pós correção modifiquei o tipo do dado de float para int