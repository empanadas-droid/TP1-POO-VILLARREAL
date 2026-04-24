import random #importamos la librería random para generar números aleatorios en el juego

#definimos la clase Hechicero con los atributos nombre, vida y mana, y los métodos para lanzar hechizos, meditar y mostrar el estado del hechicero
class Hechicero:
    def __init__(self, nombre):
        # inicializamos atributos nombre, vida y mana
        self.nombre = nombre
        self.vida = 100
        self.mana = 50
    # método para lanzar un hechizo que causa daño al objetivo y consume mana
    def LanzarHechizo(self, objetivo):
        if self.mana >= 20:
            danio = random.randint(20, 40)
            self.mana -= 20
            print(
                f"¡{self.nombre} lanza una Bola de Fuego! Causa {danio} de daño. (Mana rest.: {self.mana})"
            )
            objetivo.vida -= danio
            # aseguramos que la vida del objetivo no sea negativa
            if objetivo.vida < 0:
                objetivo.vida = 0
        else:
            print(f"¡{self.nombre} no tiene suficiente mana! El hechizo falló.")
    # método para meditar y recuperar mana
    def Meditar(self):
        recuperado = 15
        self.mana += recuperado
        print(f"{self.nombre} medita y recupera {recuperado} de mana.")
    # método para mostrar el estado actual del hechicero (vida y mana)
    def Mostrar(self):
        print(f"[{self.nombre}] Vida: {self.vida} | Mana: {self.mana}")


# Programa Principal
print("\n¡Bienvenido al Combate de Hechiceros!")
nombre_usuario = input("Ingrese el nombre de su hechicero: ").capitalize()
# creamos las instancias (objetos) para el jugador y el villano
jugador = Hechicero(nombre_usuario)
villano = Hechicero("Hechicero_Bot")

print("\n¡COMIENZA EL DUELO!")

# el combate continua hasta que uno no pueda seguir
while jugador.vida > 0 and villano.vida > 0:
    print("\n" + "=" * 30)
    jugador.Mostrar()
    villano.Mostrar()
    print("=" * 30)

    # turno del Usuario
    accion = input(
        f"\n{jugador.nombre}, ¿qué deseas hacer? (A: Atacar / M: Meditar / P: Pasar): "
    ).upper()
    # procesamos la acción del usuario y ejecutamos el método correspondiente para atacar, meditar o pasar el turno
    if accion == "A":
        jugador.LanzarHechizo(villano)
    elif accion == "M":
        jugador.Meditar()
    else:
        print(f"{jugador.nombre} decide esperar...")

    # turno del Sistema
    if villano.vida > 0:
        print("\nTurno del oponente...")
        # Si tiene mana ataca, si no, medita obligatoriamente
        if villano.mana >= 20:
            villano.LanzarHechizo(jugador)
        else:
            villano.Meditar()

# finalización del Juego
print("\n" + "*" * 30)
if jugador.vida > 0:
    print(f"¡VICTORIA! {jugador.nombre} ha ganado el duelo.")
else:
    print(f"DERROTA... {villano.nombre} te ha vencido.")

print("GAME OVER")
