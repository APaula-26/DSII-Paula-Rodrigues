#FUNÇÃO DEF | SERVE PARA DEFINIR OPERAÇÕES |

def soma (x, y):
    """ Retorna a soma de dois números."""
    return x + y 

def subtracao (x, y):
    """ Retorna a diferença de dois números."""
    return x - y 

def multiplicacao (x, y):
    """ Retorna o quociente da mutiplicação de dois números."""
    return x * y

def divisao (x, y):
    """ Retorna o quociente da divisão de dois números."""
    return x / y

def exp(x):
    """ Retorna o expoente números."""
    return x ** 2

def raiz (x):
    """ Retorna o expoente números."""
    return x ** 0.5

def memoria (resultado):
    """ Armazena o resultado da última operação na memória."""
    global ultima_operacao
    ultima_operacao = resultado
    
def mostrar_memoria():
    """ Exibe o valor armazenado na memória."""
    global ultima_operacao
    print(f"Valor na memória: {ultima_operacao}")

def main ():
    """ Execulta a calculadora."""
    while True:
        # Exibe as opções de operação
        print("-" * 20)
        print("** Calculadora **")
        print("-" * 20)
        print("| 1. Soma             |")
        print("| 2. Subtração        |")
        print("| 3. Multiplicação    |")
        print("| 4. Divisão          |")
        print("| 5. Expoente         |")
        print("| 6. Raiz             |")
        print("| 7. Memória          |")
        print("| 0. Sair             |")
        print("-" * 20)
        
        # Solicita a opção do usuário
        opcao = int(input("Digite a opção desejada: "))
        
        # Valide a opção digitada
        if opcao not in range(0,7):
            print("Opção inválida!")
            continue
        
        #Execulta a operação escolhida 
        if opcao == 1:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            resultado = soma(x,y)
            print(f"Resultado:{resultado}")
            memoria(resultado)
        elif opcao == 2:
             x = float(input("Digite o primeiro número: "))
             y = float(input("Digite o segundo número: "))
             resultado = subtracao(x,y)
             print(f"Resultado:{resultado}")
             memoria(resultado)
        elif opcao == 3:
             x = float(input("Digite o primeiro número: "))
             y = float(input("Digite o segundo número: "))
             resultado = multiplicacao(x,y)
             print(f"Resultado:{resultado}")
             memoria(resultado)
        elif opcao == 4:
             x = float(input("Digite o primeiro número: "))
             y = float(input("Digite o segundo número: "))
             resultado = divisao(x,y)
             print(f"Resultado:{resultado}")
             memoria(resultado)
        elif opcao == 5:
             x = float(input("Digite o primeiro número: "))
            #  y = float(input("Digite o segundo número: "))
             resultado = exp(x)
             print(f"Resultado:{resultado}")
             memoria(resultado)
        elif opcao == 6:
             x = float(input("Digite o primeiro número: "))
            #  y = float(input("Digite o segundo número: "))
             resultado = raiz(x)
             print(f"Resultado:{resultado}")
             memoria(resultado)
        elif opcao == 7:
            mostrar_memoria()
        elif opcao == 0:
            break

if __name__ == "__main__":
    main()   

# ________________________________________________________________________________________________________________
# Tratamento de except - trata as informações quando elas não são correspondentes ao que foi definido 

def soma(x,y):
    """Retorna a soma de dois números."""
    try:
        return float(x) + float (y)
    except ValueError:
        print("Erro: valor inválido.")
def subtracao(x,y):
    """ Retorna a diferença de dois números."""
    try:
        return float(x) - float (y)
    except ValueError:
        print("Erro: valor inválido.")
def multiplicacao(x,y):
    """Retorna o produto de dois números."""
    try:
        return float(x) * float (y)
    except ValueError:
        print("Erro: valor inválido.")
def divisao(x,y):
    """Retorna o quociente da divisão de dois números."""
    try:
        return float(x) / float (y)
    except ValueError:
        print("Erro: valor inválido.")
    except ZeroDivisionError:
        print("Erro: divisão por zero.")

# ___________________________________________________________________________________________________________________

def main():
    """ Execulta a calculadora."""
    while True:
        # ... código da função main ...

        # Executa a operação escolhida
        if opcao == 1:
            try:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                resultado = soma(x,y) 
            except ValueError:
                continue
            print(f"Resultado:{resultado}")
            memoria(resultado)
           # ...código para outras operações ...
        elif opcao == 0:
            break

if __name__ == "__main__":
    main() 