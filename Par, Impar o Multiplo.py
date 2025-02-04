def analizar_numero(numero, multiplo_de=None):
    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")

    if multiplo_de is not None:
        if numero % multiplo_de == 0:
            print(f"El número {numero} es múltiplo de {multiplo_de}.")
        else:
            print(f"El número {numero} NO es múltiplo de {multiplo_de}.")

numero = int(input("Ingrese un número: "))
multiplo_de = input("Ingrese un número para verificar si es múltiplo (o deje vacío): ")

multiplo_de = int(multiplo_de) if multiplo_de else None

analizar_numero(numero, multiplo_de)