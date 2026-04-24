import random # importamos la librería random para generar números aleatorios

# definimos la clase TorreDefensa con atributos de resistencia y nivel de escudo, y métodos para recibir ataques, reparar y mostrar el estado de la torre
class TorreDefensa:
    # inicializamos la torre con resistencia máxima y un nivel de escudo fijo
    def __init__(self):
        self.resistencia = 100
        self.nivel_escudo = 20  # capacidad de mitigar daño
    # método para recibir un ataque enemigo, calculando el daño final después de aplicar el escudo y actualizando la resistencia de la torre
    def recibir_ataque(self, danio_enemigo):
        # el daño final es el ataque enemigo menos nuestro escudo
        danio_final = danio_enemigo - random.randint(0, self.nivel_escudo)
        # aseguramos que el daño final no sea negativo (no podemos curar al recibir un ataque)
        if danio_final < 0:
            danio_final = 0
        # actualizamos la resistencia de la torre restando el daño final
        self.resistencia -= danio_final
        if self.resistencia < 0:
            self.resistencia = 0

        print(f"¡IMPACTO! La torre recibió {danio_final} de daño.")
    # método para reparar la torre, recuperando una cantidad fija de resistencia pero sin exceder el máximo
    def reparar(self):
        cura = 15
        self.resistencia += cura
        if self.resistencia > 100:
            self.resistencia = 100
        print(f"Reparando... Se han recuperado {cura} puntos de resistencia.")
    # método para mostrar el estado actual de la torre con una barra visual y el porcentaje de resistencia restante
    def mostrar_estado(self):
        # dibujamos una barra visual simple
        barra = "█" * (self.resistencia // 10) + "░" * (10 - (self.resistencia // 10))
        print(f"ESTADO DE LA TORRE: [{barra}] {self.resistencia}%")


#Programa Principal
print("\n--- ÚLTIMA DEFENSA: PROTEGE EL TERRITORIO ---")
# creamos una instancia de TorreDefensa para representar la torre que el jugador debe proteger
mi_torre = TorreDefensa()
turno = 1
# el juego continúa hasta que la torre sea destruida (resistencia llegue a 0), en cada turno el jugador puede elegir reparar la torre o esperar el ataque enemigo, luego se calcula el daño recibido y se actualiza el estado de la torre
while mi_torre.resistencia > 0:
    print(f"\n--- ONDA DE ATAQUE #{turno} ---")
    mi_torre.mostrar_estado()

    print("\n¿Qué acción tomarás?")
    print("1. Reforzar defensas (Reparar)")
    print("2. Esperar el impacto")
    opcion = input("Selecciona: ")

    if opcion == "1":
        mi_torre.reparar()

    # el enemigo siempre ataca al final del turno
    ataque_viniendo = random.randint(15, 35)
    mi_torre.recibir_ataque(ataque_viniendo)

    turno += 1

print("\n" + "X" * 30)
print("LA TORRE HA SIDO DESTRUIDA. EL TERRITORIO HA CAÍDO.")
print("X" * 30)
print(f"Resististe {turno-1} ondas de ataque.")
print("GAME OVER")
