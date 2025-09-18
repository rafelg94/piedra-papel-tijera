# voy a usar random.randint()
import random

# instrucciones y resumen del juego
print("Bienvenido/a a Piedra, Papel y Tijera, escrito en Python.")
print("El programa elegirá con qué jugar antes que tú, y te dirá lo que ha elegido cuando\nvalides tú tu elección.")

victorias = 0
derrotas = 0
empates = 0

# bucle principal del juego
while True:
    ordenador = random.choice(["Piedra", "Papel", "Tijera"])

    print(f"\n{victorias} victorias, {derrotas} derrotas, {empates} empates.")
    
    # le toca al usuario
    print("Elige (p)iedra, pape(l) o (t)ijera. Pulsa 'q' para salir del juego.")
    usuario = input("Pulsa la tecla de tu elección y luego Enter.\n")

    # salir del juego
    if usuario == "q":
        break

    # desarrollo de piedra
    elif usuario == "p":
        print("\nPiedra contra...")
        print(ordenador)
        if ordenador == "Piedra":
            print("¡Empate!")
            empates = empates + 1
            continue
        elif ordenador == "Papel":
            print("¡Derrota!")
            derrotas = derrotas + 1
            continue
        elif ordenador == "Tijera":
            print("¡Victoria!")
            victorias = victorias + 1
            continue

    # desarrollo de papel
    elif usuario == "l":
        print("\nPapel contra...")
        print(ordenador)
        if ordenador == "Papel":
            print("¡Empate!")
            empates = empates + 1
            continue
        elif ordenador == "Tijera":
            print("¡Derrota!")
            derrotas = derrotas + 1
            continue
        elif ordenador == "Piedra":
            print("¡Victoria!")
            victorias = victorias + 1
            continue

    # desarrollo de tijera
    elif usuario == "t":
        print("\nTijera contra...")
        print(ordenador)
        if ordenador == "Tijera":
            print("¡Empate!")
            empates = empates + 1
            continue
        elif ordenador == "Piedra":
            print("¡Derrota!")
            derrotas = derrotas + 1
            continue
        elif ordenador == "Papel":
            print("¡Victoria!")
            victorias = victorias + 1
            continue

    # en caso de error
    else:
        print("Pulsa una de las opciones proporcionadas (p, l, t o q, por favor.)")

print("\n\nSaliendo del juego.\nResultado final: %s victorias, %s derrotas, %s empates\n" %(victorias, derrotas, empates))
print("\nAdiós :(\n")
input("Pulsa Enter para cerrar esta ventana...")

# fin del código