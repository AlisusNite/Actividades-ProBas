def interes_compuesto(capital, tasa, tiempo, capitalizaciones=1):
    monto = capital * (1 + tasa / capitalizaciones) ** (capitalizaciones * tiempo)
    return monto

capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (en %): ")) / 100  # Convertimos a decimal
tiempo = float(input("Ingrese el tiempo en años: "))
capitalizaciones = int(input("Número de capitalizaciones por año (ej. 1 = anual, 12 = mensual): "))

monto_final = interes_compuesto(capital, tasa, tiempo, capitalizaciones)

print(f"\nEl monto final después de {tiempo} años será: {monto_final:.2f}")