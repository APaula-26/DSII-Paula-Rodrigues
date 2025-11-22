# for n in [0,18,56,77,95]:
#     print(n)
# else:
#     print("Acabou!")

    # Podemos usar o else para executar algum código após o término do loop. Vai executar o loop todo e após rodar vai 
    # apresentar a mensagem que acabou 

# for n in range(1000000):
#     print(n)
#     if n == 4:
#          break
# print("Até mais!")

    # O break serve para interromper um loop, ele quebra o loop assim que for identificado o valor desejado, ele termina
    # de executar

numeros = [1,2,3,10,12]
for numero in numeros:
    if numero == 10:
        break
    print(f"Número: {numero}")
else:
    print("Acabou")

    