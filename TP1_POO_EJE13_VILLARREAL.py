import random # importamos la librería random para generar números aleatorios

# definimos la clase Jugador con atributos de nombre y puntaje total, y un método para lanzar un dado y acumular el puntaje
class Jugador:
    #inicializamos la clase con el nombre del jugador y un puntaje total inicial de 0
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje_total = 0
    # método para lanzar un dado, generar un número aleatorio entre 1 y 6, acumular el puntaje y mostrar el resultado
    def lanzar_dado(self):
        valor = random.randint(1, 6)
        self.puntaje_total += valor
        print(f"🎲 {self.nombre} lanzó el dado y obtuvo: {valor}")
        print(f"   Puntaje acumulado: {self.puntaje_total}")


# Programa Principal
print("\n--- BIENVENIDO AL DESAFÍO DE DADOS ---")
# solicitamos el nombre del usuario para crear una instancia de Jugador
nom = input("Introduce tu nombre: ").capitalize()
usuario = Jugador(nom)
bot = Jugador("Computadora")
# el juego consiste en lanzar el dado 3 veces para cada jugador y acumular el puntaje total, luego se determina el ganador comparando los puntajes finales
rondas = 3
for r in range(1, rondas + 1):
    print(f"\n--- RONDA {r} ---")
    input("Presiona ENTER para lanzar tu dado...")
    usuario.lanzar_dado()

    print("\nAhora lanza la computadora...")
    bot.lanzar_dado()

# determinación del resultado final
print("\n" + "=" * 30)
print(
    f"RESULTADO FINAL: {usuario.nombre}: {usuario.puntaje_total} | {bot.nombre}: {bot.puntaje_total}"
)
# comparamos los puntajes totales para determinar el ganador y mostramos un mensaje acorde al resultado
if usuario.puntaje_total > bot.puntaje_total:
    print(f"¡FELICIDADES {usuario.nombre}, GANASTE EL DESAFÍO!")
elif usuario.puntaje_total < bot.puntaje_total:
    print("La computadora ha ganado esta vez.")
else:
    print("¡Es un empate!")

print("=" * 30)
print("GAME OVER")
