#definimos clase cuenta con atributos de titular y cantidad
class Cuenta:
    #inicializamos clase con los atributos titular y cantidad por teclado
    def __init__(self):
        self.titular = input(
            "Ingrese el nombre del titular de la cuenta: "
        ).capitalize()
        self.cantidad = float(input("Ingrese la cantidad inicial de dinero: "))
    #metodo para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Monto en cuenta: ${self.cantidad}")

#definimos clase caja de ahorro y plazo fijo que heredan de la clase cuenta
class CajaAhorro(Cuenta):
    #inicializamos clase con el metodo init de la clase padre
    def __init__(self):
        super().__init__()
    #metodo para mostrar los datos de la caja de ahorro
    def mostrar_informacion(self):
        print("\n--- Información Caja de Ahorro ---")
        self.mostrar()

#definimos clase plazo fijo que hereda de la clase cuenta
class PlazoFijo(Cuenta):
    #inicializamos clase con el metodo init de la clase padre y agregamos los atributos plazo e interes por teclado
    def __init__(self):
        super().__init__()
        self.plazo = int(input("Ingrese el plazo en días: "))
        self.interes = float(input("Ingrese la tasa de interés (%): "))
    #metodo para calcular el importe del interés ganado
    def obtener_importe(self):
        return self.cantidad * self.interes / 100
    #metodo para mostrar los datos del plazo fijo y el importe del interés ganado
    def mostrar_informacion(self):
        print("\n--- Información Plazo Fijo ---")
        self.mostrar()
        print(f"Plazo: {self.plazo} días")
        print(f"Interés: {self.interes}%")
        print(f"Total de interés ganado: ${self.obtener_importe()}")


# Programa Principal
caja1 = CajaAhorro()
caja1.mostrar_informacion()
plazo1 = PlazoFijo()
plazo1.mostrar_informacion()
