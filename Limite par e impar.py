def generar_listas(limite):
    pares, impares = [], []
    for num in range(limite + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares