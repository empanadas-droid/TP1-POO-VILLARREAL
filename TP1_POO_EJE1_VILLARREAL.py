# Definimos clase alumno con atributos de nombre y nota
class Alumno:
    #inicializar clase
    def inicializar(self):
        self.nombre = input("\nIngrese el nombre del alumno: ").capitalize()
        self.nota = int(input("Ingrese la nota del alumno: "))
    #metodo para determinar si el alumno esta aprobado o no
    def AlumnoAprobado(self):
        nota = self.nota
        if nota >= 7:
            print("Alumno aprobado, felicitaciones!")
        else:
            print("Alumno desaprobado, suerte para la proxima!")
    #metodo para mostrar los datos del alumno
    def mostrarAlumno(self):
        nombre = self.nombre
        nota = self.nota
        print(f"\nNombre del Alumno: {nombre}")
        print(f"Nota de {nombre}: {nota}")


# PROGRAMA PRINCIPAL
Alumno1 = Alumno()
Alumno1.inicializar()
mostrar = Alumno1.mostrarAlumno()
aprobado = Alumno1.AlumnoAprobado()
