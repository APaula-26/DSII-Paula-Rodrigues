# Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado(para ser aprovado a média deve ser no minimo 6)

nota1 = float(input('Digite a 1º nota do aluno:'))
nota2 = float(input('Digite a 2º nota do aluno:'))
media = nota1 + nota2 / 2
if media >=6:
    print(f'A média do aluno é: {media} \nAluno foi aprovado')
else:
    print('A média do aluno é:',media,'\nAluno foi reprovado')

#Correção do professor:
    # n1 = float(input('Informe a primeira nota:'))
    # n2 = float(input('Informe a primeira nota:'))
    # s = n1 + n2 / 2
    # if s >=6:
    # print(f'A média informada é: {s} Aluno foi aprovado')
    # else:
    # print('A média informada é',s,'Aluno foi aprovado')

# Após correção foi altera a função calculo para ficar somente como media mesmo. Antes estava assim: 
# calculo = nota1 + nota2 / 2
# media = calculo
    #  Com a correção ficou: media = nota1 + nota2 / 2