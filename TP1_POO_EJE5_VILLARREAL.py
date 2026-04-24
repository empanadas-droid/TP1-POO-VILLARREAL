#definimos clase agenda con atributo de contactos
class Agenda:
    def __init__(self):
        self.contactos = []
        self.menu()
    #metodo para mostrar el menu de opciones
    def menu(self):
        opcion = 0
        while opcion != 5:
            print("\n--- AGENDA ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = int(input("Elija una opción: "))
            #dependiendo de la opcion elegida se ejecuta el metodo correspondiente
            if opcion == 1:
                self.añadir()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.buscar()
            elif opcion == 4:
                self.editar()
        print("\nAgenda cerrada. ¡Hasta luego!")
    #metodo para añadir un contacto a la agenda
    def añadir(self):
        nom = input("Ingrese nombre: ").capitalize()
        tel = input("Ingrese teléfono: ")
        email = input("Ingrese email: ")
        #se agrega el contacto a la lista de contactos como un diccionario
        self.contactos.append({"nombre": nom, "tel": tel, "email": email})
    #metodo para mostrar la lista de contactos registrados en la agenda
    def listar(self):
        #si hay contactos registrados se muestra la lista, sino se muestra un mensaje indicando que no hay contactos registrados
        if self.contactos:
            print("\n--- LISTA DE CONTACTOS ---")
            for con in self.contactos:
                print(
                    f"Nombre: {con['nombre']} - Tel: {con['tel']} - Email: {con['email']}"
                )
        else:
            print("No hay contactos registrados.")
    #metodo para buscar un contacto por su nombre
    def buscar(self):
        # si hay contactos registrados se pide el nombre a buscar, sino se muestra un mensaje indicando que no hay contactos registrados
        if self.contactos:
            nom = input("Ingrese nombre a buscar: ").capitalize()
            for con in self.contactos:
                if con["nombre"] == nom:
                    print(f"Encontrado -> Tel: {con['tel']}, Email: {con['email']}")
                    return
                else:
                    print("Contacto no encontrado.")
        else:
            print("No hay contactos registrados.")
    #metodo para editar un contacto por su nombre
    def editar(self):
        # si hay contactos registrados se pide el nombre a editar, sino se muestra un mensaje indicando que no hay contactos registrados
        if self.contactos:
            nom = input("Ingrese nombre a editar: ").capitalize()
            for con in self.contactos:
                if con["nombre"] == nom:
                    con["tel"] = input("Ingrese nuevo teléfono: ")
                    con["email"] = input("Ingrese nuevo email: ")
                    print("Contacto actualizado.")
                    return
                else:
                    print("Contacto no encontrado.")
        else:
            print("No hay contactos registrados.")


# Programa Principal
agenda1 = Agenda()
