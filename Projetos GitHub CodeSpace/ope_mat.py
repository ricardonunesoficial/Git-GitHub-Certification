import math

def calcular_pi_entre_numeros():
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
    resultado = produto * math.pi
    
    # Exibir o resultado
    print(f"O resultado da equação é: {resultado}")

# Chamada da função
calcular_pi_entre_numeros()