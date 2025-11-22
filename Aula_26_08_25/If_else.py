#IF ->

#  media = float(input('Digite a media do aluno:'))
# if media > 5:
#     print('A media informada é:',media,'\nAluno foi aprovado')

    # quando colocado o f atribuimos uma função.Então quando colocamos a {media} ele considera apresentar o resultado pois atribuimos uma função  
    # print(f'A media informada é: {media} \nAluno foi aprovado')

# IF E ELSE ->

# media = float(input('Digite a media do aluno:'))
# if media >=5:
#     print(f'A media informada é: {media} \nAluno foi aprovado')
# else:
#     print('A media informada é:',media,'\nAluno foi reprovado')

#ELIF - usando quando o parametro é "e se". 

media = float(input('Digite a media do aluno:'))
if media >=5:
    print(f'A média informada é: {media} \nAluno foi aprovado')
elif media >= 4 and media <=4.9:
    print('A média informada é:',media,'\nAluno ficou de recuperação')
else:
    print('A média informada é:',media,'\nAluno foi reprovado')