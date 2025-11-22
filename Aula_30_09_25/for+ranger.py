for n1 in range(20):
    print(n1)

# Range: vai pegar o parametro que inseriu dentro da declaração da função e exibir. Exemplo acima: ele declara a 
# função for e dentro da variavel n1 ele chama a função range(20), então isso define que ao exibir no print o n1
# o ranger vai exibir os números até 20. 

for n1 in range(1,100,1):
    print(n1)

# Definindo mais parametro no ranger ele executa da forma acima, onde range(1,100,1), aqui ele defini que a contagem
# do número começa em 1, vai até o 100 e vai contando de 1 em 1. Se quisessemos de 2 em 2, até o 100, iriamos declarar como:
# range(1,100,2)
    
    # Ou seja, o primeiro parametro é onde começa, o segundo é até que número deseja que conte e o último define 
    # de quanto em quanto.