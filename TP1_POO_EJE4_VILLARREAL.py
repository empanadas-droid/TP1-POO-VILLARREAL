#definimos clase calculadora con atributos de num1 y num2
class Calculadora:
    #inicializamos clase
    def __init__(self):
        self.num1 = int(input("Ingrese numero 1: "))
        self.num2 = int(input("Ingrese numero 2: "))
    #metodo para sumar los numeros
    def Sumar(self):
        suma = self.num1 + self.num2
        print(f"\n~El resultado de la suma entre los numeros es: {suma}")
    #metodo para restar los numeros
    def Restar(self):
        resta = self.num1 - self.num2
        print(f"~El resultado de la resta entre los numeros es: {resta}")
    #metodo para multiplicar los numeros
    def Multiplicar(self):
        multi = self.num1 * self.num2
        print(f"~El resultado de la multiplicacion entre los numeros es: {multi}")
    #metodo para dividir los numeros
    def Dividir(self):
        divi = self.num1 / self.num2
        print(f"~El resultado de la division entre los numeros es: {divi}")
    #metodo para mostrar los numeros ingresados
    def MostrarCalculadora(self):
        print(f"\nNumero 1: {self.num1}")
        print(f"Numero 2: {self.num2}")

# Programa Principal
print("\n--- CALCULADORA ---")
calculadora1 = Calculadora()
calculadora1.MostrarCalculadora()
suma = calculadora1.Sumar()
resta = calculadora1.Restar()
multiplicacion = calculadora1.Multiplicar()
division = calculadora1.Dividir()
