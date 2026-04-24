#definimos clase triangulo con atributos de lado1, lado2 y lado3
class Triangulo:
    #inicializamos clase
    def inicializar(self):
        self.lado1 = int(input("Ingrese longitud del primer lado del triangulo: "))
        self.lado2 = int(input("Ingrese longitud del segundo lado del triangulo: "))
        self.lado3 = int(input("Ingrese longitud del tercer lado del triangulo: "))
    #metodo para mostrar el lado mayor del triangulo
    def MostrarLadoMayor(self):
        lados = [self.lado1, self.lado2, self.lado3]
        mayor = lados[0]
        for i in range(len(lados)):
            if lados[i] > mayor:
                mayor = lados[i]
        print(f"~El lado mayor del triangulo es: {mayor}")
    #metodo para determinar el tipo de triangulo
    def SaberTipo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("~El triangulo es: Equilatero (todos los angulos son iguales).")
        elif (
            self.lado1 == self.lado2
            or self.lado1 == self.lado3
            or self.lado2 == self.lado3
        ):
            print("~El triángulo es: Isósceles (dos lados iguales y uno diferente)")
        else:
            print("~El triángulo es: Escaleno (todos los angulos son diferentes)")
    #metodo para mostrar los lados del triangulo
    def MuestroTriangulo(self):
        print(f"\nValores de cada lado: {self.lado1}, {self.lado2}, {self.lado3}")


# Programa Principal
print("\n--- TRIANGULOS Y SU TIPO ---")
triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.MuestroTriangulo()
triangulo1.SaberTipo()
triangulo1.MostrarLadoMayor()
