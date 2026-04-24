import random # importamos la librería para generar números aleatorios

# definimos la clase Explorador con atributos de nombre y monedas
class Explorador:
    #inicializamos la clase con el nombre del explorador y un contador de monedas
    def __init__(self, nombre):
        self.nombre = nombre
        self.monedas = 0  #el recurso acumulado
    #metodo para recolectar monedas de un cofre
    def recolectar(self, cofre):
        # verificamos que el cofre esté abierto para recolectar su contenido
        if cofre.estado == "abierto":
            # verificamos que el cofre tenga contenido para recolectar
            if cofre.contenido > 0:
                print(f"¡Genial! Has recogido {cofre.contenido} monedas.")
                self.monedas += cofre.contenido
                cofre.contenido = 0  # el cofre queda vacío
            else:
                print("Este cofre ya está vacío.")
        else:
            print("No puedes recolectar nada, el cofre está cerrado.")

#definimos la clase Cofre con atributos de estado y contenido
class Cofre:
    #inicializamos la clase con el estado cerrado y un contenido aleatorio de monedas
    def __init__(self):
        self.estado = "cerrado"
        self.contenido = random.randint(10, 50)  #monedas aleatorias
    #metodo para abrir el cofre y cambiar su estado a abierto
    def abrir(self):
        self.estado = "abierto"
        print("Has abierto el cofre. ¡Brilla por dentro!")


#Programa Principal
print("\n--- EL TESORO ESCONDIDO ---")
# solicitamos el nombre del jugador y creamos una instancia de Explorador
nombre_jugador = input("Ingresa el nombre de tu explorador: ").capitalize()
jugador = Explorador(nombre_jugador)
#creamos el primer cofre para iniciar la aventura
cofre_actual = Cofre()
print(f"\n¡Bienvenido, {jugador.nombre}! Te encuentras en una cueva misteriosa.")
print("Tu objetivo es encontrar y recolectar la mayor cantidad de monedas posible.")
print("¡Buena suerte en tu aventura!")
# bucle principal del juego: el jugador puede elegir abrir el cofre, recolectar monedas, seguir explorando o salir de la cueva
continuar = True
while continuar:
    # mostramos el estado actual del cofre y las monedas acumuladas del jugador
    print(f"\nEstado del cofre: {cofre_actual.estado}")
    print(f"Monedas totales de {jugador.nombre}: {jugador.monedas}")

    print("\n¿Qué quieres hacer?")
    print("1. Intentar abrir cofre")
    print("2. Recolectar monedas")
    print("3. Seguir explorando (Nuevo cofre)")
    print("4. Salir de la cueva")

    opcion = input("Selecciona una opción: ")
    # procesamos la opción elegida por el jugador y ejecutamos la acción correspondiente
    if opcion == "1":
        cofre_actual.abrir()
    elif opcion == "2":
        jugador.recolectar(cofre_actual)
    elif opcion == "3":
        print("Caminas por la cueva y encuentras otro cofre...")
        cofre_actual = Cofre()  #nuevo cofre con contenido aleatorio
    elif opcion == "4":
        continuar = False
# al finalizar el juego, mostramos el total de monedas recolectadas por el jugador
print(f"\n{jugador.nombre} salió de la cueva con {jugador.monedas} monedas.")
print("GAME OVER")
