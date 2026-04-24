import random #importamos la librería random para generar números aleatorios en el juego

#definimos la clase Aventurero con los atributos nombre y una lista de inventario, y los métodos para guardar objetos, utilizar objetos y consultar el inventario
class Aventurero:
    def __init__(self, nombre):
        # inicializa el nombre y una lista vacía para objetos
        self.nombre = nombre
        self.inventario = []
    # método para guardar un objeto en el inventario
    def guardar_objeto(self, objeto):
        # añadimos un elemento a la lista dinámica
        self.inventario.append(objeto)
        print(f"\n[SISTEMA] {self.nombre} ha guardado '{objeto}' en su mochila.")
    # método para utilizar un objeto del inventario
    def utilizar_objeto(self):
        # mostramos los objetos para que el usuario elija cual usar
        if not self.inventario:
            print("\n[ERROR] No tienes objetos para utilizar.")
        else:
            self.consultar_mochila()
            objeto_usar = input("¿Qué objeto deseas utilizar?: ").lower()
            # verificamos si el objeto está en el inventario y lo eliminamos si se utiliza
            if objeto_usar in self.inventario:
                self.inventario.remove(objeto_usar)
                print(
                    f"\n[SISTEMA] Has utilizado '{objeto_usar}'. El objeto ha desaparecido de tu inventario."
                )
            else:
                print(f"\n[ERROR] El objeto '{objeto_usar}' no está en tu mochila.")
    # método para consultar el inventario y mostrar los objetos que el aventurero tiene
    def consultar_mochila(self):
        # recorremos la lista para mostrar la información actual
        print(f"\n--- MOCHILA DE {self.nombre} ---")
        # si la lista está vacía mostramos un mensaje, sino mostramos los objetos disponibles
        if not self.inventario:
            print("Tu mochila está vacía.")
        else:
            #con la funcion enumerate mostramos el índice y el objeto para facilitar la selección al usuario
            for i, objeto in enumerate(self.inventario, 1):
                print(f"{i}. {objeto}")
        print("---------------------------")


# Programa Principal
print("\n--- BIENVENIDO A LA AVENTURA ---")
# solicitamos el nombre del jugador y creamos una instancia de Aventurero
nom = input("Introduce el nombre de tu aventurero: ").capitalize()
jugador = Aventurero(nom)

# lista de objetos que se pueden encontrar en el camino
objetos_posibles = [
    "espada de madera",
    "poción de vida",
    "escudo de cuero",
    "mapa antiguo",
    "antorcha",
    "piedra mágica",
    "llave misteriosa",
    "cuerda resistente",
    "botella de agua",
    "amuleto de la suerte",
]
# bucle principal del juego donde el jugador puede elegir explorar, consultar su mochila, utilizar un objeto o abandonar la aventura
continuar = True
while continuar:
    print("\n¿Qué deseas hacer?")
    print("1. Explorar el escenario")
    print("2. Ver mi mochila")
    print("3. Utilizar un objeto")
    print("4. Abandonar la aventura")

    opcion = input("Selecciona una opción: ")
    # procesamos la opción elegida por el jugador y ejecutamos la acción correspondiente
    if opcion == "1":
        # simulamos encontrar un objeto al azar
        hallazgo = random.choice(objetos_posibles)
        print(f"\n¡Has encontrado un/a: {hallazgo}!")
        decision = input("¿Deseas guardarlo? (S/N): ").upper()
        if decision == "S":
            jugador.guardar_objeto(hallazgo)
        else:
            print(f"Has dejado el/la {hallazgo} en el suelo.")

    elif opcion == "2":
        jugador.consultar_mochila()

    elif opcion == "3":
        jugador.utilizar_objeto()

    elif opcion == "4":
        print(f"\n{jugador.nombre} ha decidido retirarse del camino.")
        continuar = False
    else:
        print("\nOpción no válida.")

print("\nHas finalizado tu viaje.")
print("GAME OVER")
