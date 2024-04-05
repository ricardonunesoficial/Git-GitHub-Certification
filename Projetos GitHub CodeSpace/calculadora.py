import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    return math.sqrt(a)

def porcentagem(a, b):
    return (a * b) / 100

def calcular():
    while True:
        print("\nCalculadora:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Porcentagem")
        print("8. Sair")

        opcao = input("\nEscolha a operação (1-8): ")

        if opcao in ['1', '2', '3', '4', '5', '7']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        elif opcao == '6':
            a = float(input("Digite o número: "))
        elif opcao == '8':
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == '1':
            print(f"Resultado: {somar(a, b)}")
        elif opcao == '2':
            print(f"Resultado: {subtrair(a, b)}")
        elif opcao == '3':
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcao == '4':
            print(f"Resultado: {dividir(a, b)}")
        elif opcao == '5':
            print(f"Resultado: {potencia(a, b)}")
        elif opcao == '6':
            print(f"Resultado: {raiz_quadrada(a)}")
        elif opcao == '7':
            print(f"Resultado: {porcentagem(a, b)}")

# Chamada da função para iniciar a calculadora
calcular()