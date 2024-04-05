def processar_strings():
    # Solicitar as strings
    strings = input("Digite várias strings separadas por espaço: ").split()
    
    # Solicitar o número de repetições
    numero_repeticoes = int(input("Digite o número de repetições: "))
    
    # Dicionário para armazenar as strings e o número de repetições
    strings_repetidas = {}
    
    # Iterar sobre as strings
    for string in strings:
        # Verificar se a string já está no dicionário
        if string in strings_repetidas:
            # Se estiver, adicionar ao valor existente
            strings_repetidas[string] += numero_repeticoes
        else:
            # Se não estiver, adicionar ao dicionário com o valor inicial
            strings_repetidas[string] = numero_repeticoes
    
    # Exibir as strings e o número de repetições
    for string, repeticoes in strings_repetidas.items():
        print(f"{string}: {repeticoes}")
    
    # Realizar operações matemáticas com as strings
    soma = sum(map(len, strings_repetidas.keys()))
    media = soma / len(strings_repetidas)
    print(f"Soma dos tamanhos das strings: {soma}")
    print(f"Média dos tamanhos das strings: {media}")

# Chamada da função
processar_strings()