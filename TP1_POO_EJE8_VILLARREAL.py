import random  #libreria para valores aleatorios


class Personaje:
    def __init__(self, nombre, vida, danio):
        #inicializamos los atributos básicos de los personajes
        self.nombre = nombre
        self.vida = vida
        self.danio = danio

    def Mostrar(self):
        #mostramos el estado actual del participante en cada turno
        print(f"[{self.nombre}] Vida: {self.vida} | Daño Base: {self.danio}")

    def Atacar(self, enemigo):
        # verificamos que el atacante pueda luchar
        if self.vida > 0:
            # generamos un daño aleatorio basado en su capacidad
            golpe = random.randint(5, self.danio + 10)
            enemigo.vida -= golpe
            print(f"-> {self.nombre} golpea a {enemigo.nombre} por {golpe} de daño.")

            # evitamos que la vida sea negativa
            if enemigo.vida < 0:
                enemigo.vida = 0
        else:
            print(f"{self.nombre} ya no puede luchar.")


# Programa Principal 
print("\n¡Bienvenido a la Arena de Combate de Personajes!")
# Creamos las instancias (objetos) para el jugador y el villano
nombre_usuario = input("Ingrese el nombre de su héroe: ").capitalize()
jugador = Personaje(nombre_usuario, 100, 15)
villano = Personaje("Sistema_Bot", 100, 15)

print("\n¡COMIENZA EL DUELO EN LA ARENA!")

# bucle de combate: continua mientras ambos tengan vida
while jugador.vida > 0 and villano.vida > 0:
    print("\n" + "=" * 30)
    jugador.Mostrar()
    villano.Mostrar()
    print("=" * 30)

    #turno del usuario
    accion = input(
        f"\n{jugador.nombre}, ¿qué deseas hacer? (A: Atacar / P: Pasar): "
    ).upper()
    #procesamos la acción del usuario
    if accion == "A":
        jugador.Atacar(villano)
    else:
        print(f"{jugador.nombre} decide esperar...")

    #turno del Sistema (Automático)
    if villano.vida > 0:
        print("\nTurno del oponente...")
        villano.Atacar(jugador)

# finalización del Juego
print("\n" + "*" * 30)
if jugador.vida > 0:
    print(f"¡VICTORIA! {jugador.nombre} ha ganado el duelo.")
else:
    print(f"DERROTA... {villano.nombre} te ha vencido.")

print("GAME OVER")
