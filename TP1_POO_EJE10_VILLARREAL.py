import random #importamos la libreria random para generar valores aleatorios

# definimos la clase Auto con atributos de modelo, posición, velocidad y meta final
class Auto:
    #inicializamos clase
    def __init__(self, modelo):
        self.modelo = modelo
        self.posicion = 0
        self.velocidad = 0
        self.meta_final = 200  # Definimos la meta como atributo
    #metodo para acelerar el auto, aumentando su velocidad y posición
    def acelerar(self):
        #incrementamos la velocidad con un valor aleatorio entre 10 y 25
        incremento = random.randint(10, 25)
        self.velocidad += incremento
        self.posicion += self.velocidad
        # aseguramos que no pase de la meta en el dibujo
        if self.posicion > self.meta_final:
            self.posicion = self.meta_final

    #metodo para frenar el auto, disminuyendo su velocidad y posición
    def frenar(self):
        #disminuimos la velocidad en 10 unidades, pero no permitimos que sea negativa
        self.velocidad -= 10
        if self.velocidad < 0:
            self.velocidad = 0
        #actualizamos la posición con la nueva velocidad
        self.posicion += self.velocidad
        if self.posicion > self.meta_final:
            self.posicion = self.meta_final
    #metodo para avanzar automáticamente el auto rival con una velocidad aleatoria
    def avanzar_automatico(self):
        avance = random.randint(15, 40)
        self.posicion += avance
        #aseguramos que no pase de la meta en el dibujo
        if self.posicion > self.meta_final:
            self.posicion = self.meta_final
    #metodo para dibujar la pista de carrera con la posición actual del auto
    def dibujar_pista(self):
        #escalamiento: 200 metros reales = 20 caracteres en pantalla
        largo_pista = 20
        posicion_visual = int((self.posicion / self.meta_final) * largo_pista)

        #creamos la pista: espacios en blanco, el auto y la meta
        #utilizamos la función ljust para alinear el nombre del auto a la izquierda y mostrar la pista con el auto en su posición actual
        pista = "_" * posicion_visual + "🏎️" + "_" * (largo_pista - posicion_visual)
        print(f"{self.modelo.ljust(12)} |{pista}| FIN")


#Programa Principal
print("\n" + "=" * 40)
print("       ARRANCA LA GRAN CARRERA")
print("=" * 40)
#solicitamos el nombre del auto del jugador y creamos una instancia de Auto para el jugador y otro para el rival
nombre_usuario = input("Nombre de tu auto: ").capitalize()
mi_auto = Auto(nombre_usuario)
rival = Auto("Rival_CPU")
#iniciamos la carrera con un bucle que continúa hasta que uno de los autos alcance o supere la meta final
ronda = 1
while mi_auto.posicion < 200 and rival.posicion < 200:
    print(f"\n--- Turno {ronda} ---")

    # dibujamos a ambos competidores
    mi_auto.dibujar_pista()
    rival.dibujar_pista()
    # solicitamos la acción del jugador: acelerar o frenar
    print("\n¿Acción?")
    print("1. Acelerar")
    print("2. Frenar")
    opcion = input(">> ")
    # procesamos la acción elegida por el jugador y ejecutamos el método correspondiente para acelerar o frenar su auto
    if opcion == "1":
        mi_auto.acelerar()
    else:
        mi_auto.frenar()
    # el auto rival avanza automáticamente con una velocidad aleatoria cada turno
    rival.avanzar_automatico()
    ronda += 1

# Dibujo Final y Resultado
print("\n--- POSICIONES FINALES ---")
mi_auto.dibujar_pista()
rival.dibujar_pista()

print("\n" + "*" * 40)
if mi_auto.posicion >= 200 and mi_auto.posicion >= rival.posicion:
    print(f"¡VICTORIA! {mi_auto.modelo} ganó la carrera.")
else:
    print(f"DERROTA... {rival.modelo} llegó primero.")
print("*" * 40)

print("\nGAME OVER")
