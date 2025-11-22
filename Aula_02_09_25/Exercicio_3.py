# Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias: 
# infantil A = 5 a 7 anos  | infantil B = 8 a 11 anos | juvenil A = 12 a 13 anos | Juvenil B = 14 a 17 anos
# Adultos = Maiores de 18 anos 

I = int(input("Informe a idade do nadador:"))
idade = I
if idade >=5 and idade <=7:
    print("Pertence a categoria Infantil A")
elif idade >=8 and idade <=11:
    print("Pertence a categoria Infantil B") 
elif idade >=12 and idade <=13:
    print("Pertence a categoria Juvenil A")
elif idade >=14 and idade <=17:
    print("Pertence a categoria Juvenil B")
elif idade >=18:
    print("Pertence a categoria Adultos")
else: 
    print ("Ainda não há turmas para está faixa etária!!")



