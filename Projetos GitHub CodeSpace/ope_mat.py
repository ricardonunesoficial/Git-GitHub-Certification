import math

def calcular_operacao_completa():
    # Solicitar os 5 números
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    
    # Calcular o produto dos números
    produto = 1
    for numero in numeros:
        produto *= numero
    
    # Multiplicar pelo valor de pi
    resultado_pi = produto * math.pi
    
    # Calcular a raiz quadrada do resultado
    resultado_final = math.sqrt(resultado_pi)
    
    # Exibir o resultado
    print(f"O resultado da operação é: {resultado_final}")

# Chamada da função
calcular_operacao_completa()
