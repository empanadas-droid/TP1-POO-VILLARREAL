#definimos clase persona con atributos de nombre y edad
class Persona:
    #inicializamos clase
    def inicializar(self):
        self.nombre = input("\nIngrese el nombre de la persona: ").capitalize()
        self.edad = int(input("Ingrese la edad de la persona: "))
    #metodo para determinar si la persona es mayor de edad o no
    def MayorEdad(self):
        edad = self.edad
        if edad >= 18:
            print("Persona mayor de edad.")
        else:
            print("Persona menor de edad.")
        return
    #metodo para mostrar los datos de la persona
    def MuestroPersona(self):
        nombre = self.nombre
        edad = self.edad
        print(f"\nNombre de la persona: {nombre}")
        print(f"Edad de {nombre}: {edad}")


# Programa Principal
Persona1 = Persona()
Persona1.inicializar()
mostrar = Persona1.MuestroPersona()
mayor = Persona1.MayorEdad()
