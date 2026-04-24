#definimos clase cliente con atributos de nombre y cantidad
class Cliente:
    def __init__(self):
        # inicializamos los atributos nombre y cantidad por teclado
        self.nombre = input("Ingrese el nombre del cliente: ").capitalize()
        self.cantidad = float(input("Ingrese la cantidad inicial: "))

    def depositar(self, monto):
        # sumamos el monto al atributo cantidad del objeto
        self.cantidad += monto
        print(f"{self.nombre} ha depositado ${monto}.Nuevo saldo: ${self.cantidad}")

    def extraer(self, monto):
        # restamos el monto al atributo cantidad
        self.cantidad -= monto
        print(f"{self.nombre} ha extraído ${monto}.Nuevo saldo: ${self.cantidad}")

    def mostrar_total(self):
        # mostramos el nombre y la cantidad actual
        print(f"{self.nombre} tiene un saldo de: ${self.cantidad}")

    def retornar_monto(self):
        # método auxiliar para que el banco pueda acceder al valor
        return self.cantidad


class Banco:
    def __init__(self):
        # la clase banco tiene como atributos 3 objetos de la clase cliente
        print("\n--- Registro de Clientes ---")
        self.cliente1 = Cliente()
        self.cliente2 = Cliente()
        self.cliente3 = Cliente()

    def operar(self):
        # ejecutamos metodos de deposito y extraccion para probar el sistema
        print("\n--- Realizando Operaciones ---")
        self.cliente1.depositar(500)
        self.cliente2.depositar(1000)
        self.cliente3.extraer(200)

    def deposito_total(self):
        # calculamos la suma de las cantidades de los 3 clientes
        total = (
            self.cliente1.retornar_monto()
            + self.cliente2.retornar_monto()
            + self.cliente3.retornar_monto()
        )

        print("\n--- Resultados del día ---")
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()
        print(f"La cantidad total de dinero en el banco es: ${total}")


# Programa Principal
banco_central = Banco()
banco_central.operar()
banco_central.deposito_total()
