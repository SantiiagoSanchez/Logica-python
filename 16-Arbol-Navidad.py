import random

class ArbolNavidad():

    def __init__(self, altura: int):
        self.altura = altura
        self.arbol = [[" " for _ in range(2 * altura - 1)] for _ in range(altura)]
        for i in range(altura):
            for j in range(altura - i - 1, altura + i):
                self.arbol[i][j] = "*"
        
        self.tronco = [[" " for _ in range(2 * altura - 1)] for _ in range(2)]

        for i in range(2):
            for j in range(altura - 2, altura + 1):
                self.tronco[i][j] = "|"

        self.estrella = False
        self.bolas = []
        self.luces = []
        self.luces_on = False

    def imprimirArbol(self):
        for index, row in enumerate(self.arbol):
            if index == 0 and self.estrella:
                print("".join(row).replace("*", "@"))
            else:
                print("".join(row))

        for row in self.tronco:
            print("".join(row))

    def add_Estrella(self):
        if self.estrella:
            print("La estrella ya existe en el arbol.")
        else:
            self.estrella = True
            print("Se añadio la estrella en el arbol")

    def borrar_Estrella(self):
        if not self.estrella:
            print("No hay estrellas en el arbol. No se puede quitar.")
        else:
            self.estrella = False
            print("Se removio la estrella en el arbol")

    def add_bolas(self):
        disponible = self.disponible()

        if len(disponible) < 2:
            print("No queda espacio en el arbol para las bolas.")
        else:
            bolas_seleccionadas = random.sample(disponible, 2)

            for i, j in bolas_seleccionadas:
                self.arbol[i][j] = "o"
                self.bolas.append((i, j))
            print("Se añadieron bolas al arbol.")

    def borrar_bolas(self):
        if len(self.bolas) < 2:
            print("No hay bolas para quitar.")
        else:
            bolas_seleccionadas = random.sample(self.bolas, 2)

            for i, j in bolas_seleccionadas:
                self.arbol[i][j] = "*"
                self.bolas.remove((i, j))
            print("Se eliminaron bolas del arbol.")
    
    def add_Luces(self):
        disponible = self.disponible()

        if len(disponible) < 3:
            print("No queda espacio en el arbol para las luces.")
        else:
            luces_seleccionadas = random.sample(disponible, 3)

            for i, j in luces_seleccionadas:
                self.arbol[i][j] = "+" if self.luces_on else "*"
                self.luces.append((i, j))
            print("Se añadieron luces al arbol.")

    def borrar_Luces(self):
        if len(self.luces) < 3:
            print("No hay luces para quitar.")
        else:
            bolas_seleccionadas = random.sample(self.luces, 3)

            for i, j in bolas_seleccionadas:
                self.arbol[i][j] = "*"
                self.luces.remove((i, j))
            print("Se eliminaron luces del arbol.")

    def interruptor_luces(self, activo):
        if not self.luces:
            print("No hay luces en el arbol.")
            

        self.luces_on = activo
        for i, j in self.luces:
            self.arbol[i][j] = "+" if activo else "*"
            print(f"Las luces fueron {'encendidas' if activo else 'apagadas'}.")


    def disponible(self):
        disponible_arbol = [
            (i, j) for i in range(1, self.altura) for j in range(
                self.altura - i - 1, self.altura + i) if self.arbol[i][j] == "*"
        ]

        if not self.luces_on:
            for i, j in self.luces:
                disponible_arbol.remove((i, j))
        return disponible_arbol



altura = input("Ingresa la altura que quieres que tenga tu arbol: ")

if altura.isdigit() and int(altura) > 0:
    arbolito = ArbolNavidad(int(altura))
    
    while True:
        arbolito.imprimirArbol()

        print("\nAcciones:")
        print("1. Añadir estrella")
        print("2. Quitar estrella")
        print("3. Añadir bolas")
        print("4. Quitar bolas")
        print("5. Añadir luces")
        print("6. Quitar luces")
        print("7. Encender luces")
        print("8. Apagar luces")
        print("9. Salir")

        accion = input("Selecciona una opcion: ")

        match accion:
            case "1":
                arbolito.add_Estrella()
            case "2":
                arbolito.borrar_Estrella()
            case "3":
                arbolito.add_bolas()
            case "4":
                arbolito.borrar_bolas()
            case "5":
                arbolito.add_Luces()
            case "6":
                arbolito.borrar_Luces()
            case "7":
                arbolito.interruptor_luces(True)
            case "8":
                arbolito.interruptor_luces(False)
            case "9":
                print("Saliendo del programa")
                break
            case _:
                print("ERROR: Opcion no valida.")
else:
    print(f"ERROR: Altura '{altura}' no valida.")