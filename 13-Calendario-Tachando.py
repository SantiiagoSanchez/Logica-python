class Calendario:

    def __init__(self):
        self.dias = [False] * 24


    def mostrar_calendario(self):
        for row in range(0, 24, 6):
            print("**** " * 6)
            print(" ".join([ f"*{str(dia).zfill(2)}*" if not self.dias[dia - 1] else "****" for dia in range(row + 1, row + 7)]))
            print("**** " * 6)
            print()

    def select_dia(self, dia):

        is_digit = dia.isdigit()

        if is_digit and int(dia) > 0 and int(dia) <= 24:
            dia = int(dia)
            if self.dias[dia - 1]:
                print(f"El dia {dia} ya ha sido seleccionado antes.")
            else:
                self.dias[dia - 1] = True
                print(f"Has seleccionado el dia {dia}.")
        else:
            print("ERROR: Debes introducir un numero (entre 1 - 24).")


calendary = Calendario()

while True:
    calendary.mostrar_calendario()
    seleccion = input("Selecciona un dia para tacharlo o escribe 'salir' para finalizar: ")

    if seleccion.lower() == "salir":
        print("Saliendo del calendario..")
        break

    calendary.select_dia(seleccion)
