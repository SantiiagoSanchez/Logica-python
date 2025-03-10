matriz = [
    ["🧑","⬛","⬜","⬛","⬛","⬛"],
    ["⬜","⬜","⬜","⬜","⬜","⬜"],
    ["⬜","⬛","⬜","⬛","⬜","⬛"],
    ["⬜","⬛","⬜","⬜","⬜","⬜"],
    ["⬜","⬛","⬛","⬜","⬛","⬜"],
    ["⬜","⬛","⬛","⬜","⬛","🚪"]
]

def printMatriz():   #Imprimir el laberinto
    for row in matriz:
        print(" ".join(row))
    print()


persona = [0, 0] #Posicion inicial

while True:

    printMatriz()

    direccion = input("A donde quieres moverte? (Arriba, Abajo, Izquierda, Derecha): ")

    filaActual, columnaActual = persona
    filaNueva, columnaNueva = filaActual, columnaActual

    match direccion.lower():
        case "arriba":
            filaNueva = filaActual - 1
        case "abajo":
            filaNueva = filaActual + 1
        case "izquierda":
            columnaNueva = columnaActual - 1
        case "derecha":
            columnaNueva = columnaActual + 1
        case _:
            print("ERROR: Hay que poner una direccion correcta (Arriba, Abajo, Izquierda, Derecha)\n")
            continue

    if filaNueva < 0 or filaNueva > 5 or columnaNueva > 5 or columnaNueva < 0:
        print("No puedes desplazarte afuera del laberinto\n")
        continue
    else:
        if matriz[filaNueva][columnaNueva] == "⬛":
            print("OBSTACULO: No se puede pasar\n")
            continue
        elif matriz[filaNueva][columnaNueva] == "🚪":
            print("¡FELICITACIONES: Has encontrado la salida.!")
            matriz[filaActual][columnaActual] = "⬜"
            matriz[filaNueva][columnaNueva] = "🧑"
            printMatriz()
            break
        else:
            matriz[filaActual][columnaActual] = "⬜"
            matriz[filaNueva][columnaNueva] = "🧑"
            persona = filaNueva, columnaNueva

    printMatriz()
