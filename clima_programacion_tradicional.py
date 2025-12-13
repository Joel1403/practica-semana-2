def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de una semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula y retorna el promedio semanal de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    temperaturas_semana = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas_semana)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()
