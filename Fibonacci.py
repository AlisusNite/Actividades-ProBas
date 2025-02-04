def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia[:n]


num = int(input("Ingresa el número de términos de Fibonacci: "))


if num <= 0:
    print("Ingresa un número entero positivo.")
else:
    print(f"Secuencia de Fibonacci ({num} términos): {fibonacci(num)}")
