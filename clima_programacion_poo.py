class Clima:
    def __init__(self):
        # Atributo encapsulado
        self._temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias de una semana.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal.
        """
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(Clima):
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()


if __name__ == "__main__":
    main()
