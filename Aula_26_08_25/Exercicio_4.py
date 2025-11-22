# Escreva um programa que pergunte o ano de nascimento de uma pessoa e diga se ele é maior de idade. 

ano = int(input('Informe o ano do seu nascimento:'))
idade = 2025 - ano
if idade >= 18:
    print('Parabéns! Você é maior de idade.')
else:
    print('Oou! Você ainda não é maior de idade.')


# Correção do professor:
    # x = int(input('Informe o ano de nascimento:'))
    # idade = 2025 - x 
    # if idade >=18:
    # print(f'Você é maior de idade {idade}')
    # else
    # print (f'Você é menor de idade {idade}')

# Após correção foi modificado o parametro passado de <=2007 para:
    # idade = 2025 - ano
    # if idade >= 18:
# Além disso foi mudado de float para int