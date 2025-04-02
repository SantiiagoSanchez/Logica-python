import os


MESES = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


def mostrar_menu():
    print("\nPlanificador de objetivos:")
    print("1. Añadir objetivo")
    print("2. Calcular el plan detallado")
    print("3. Guardar la planificación")
    print("4. Salir")


class Objetivo():

    def __init__(self, nombre_objetivo: str, cantidad: int, unidades: str, limite: int):
        self.nombre_objetivo = nombre_objetivo
        self.cantidad = cantidad
        self.unidades = unidades
        self.limite = limite


def request_objetivo() -> Objetivo:

    nombre_objetivo = input("Objetivo: ")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("ERROR: Debes colocar un numero positivo")
                continue

            break
        except Exception as e:
            print(f"ERROR: {e}")

    unidades = input("Unidades: ")

    while True:
        try:
            limite = int(input("Plazo en meses (maximo 12): "))
            if limite <= 0 or limite > len(MESES):
                print("ERROR: Tienes que ingresar un valor entre (1-12)")
                continue

            break

        except Exception as e:
            print(f"ERROR: {e}")

    return Objetivo(nombre_objetivo, cantidad, unidades, limite)

def calcular_plan(objetivos : list[Objetivo]) -> dict:

    plan = {mes : [] for mes in range(1, len(MESES) + 1)}

    for objetivo in objetivos:

        cantidad_mes = objetivo.cantidad / objetivo.limite

        for mes in range(1, objetivo.limite + 1):
            plan[mes].append(Objetivo(objetivo.nombre_objetivo, round(cantidad_mes, 2), objetivo.unidades, objetivo.cantidad))

    return plan

def mostrar_plan(plan: dict):
    for mes in range(1, len(MESES) + 1):
        if not plan[mes]:
            #No hay objetivos en este mes
            break
        
        print(f"\n{MESES[mes - 1]}: ")

        for index, objetivo in enumerate(plan[mes], start=1):
            print(f"[ ] {index}. {objetivo.nombre_objetivo} ({objetivo.cantidad} {objetivo.unidades}/mes) Total: {objetivo.limite}.")

def guardar_plan(plan: dict):

    fichero_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plan.txt")

    with open(fichero_path, "w", encoding="utf-8") as file:
        file.write("Plan detallado")

        for mes in range(1, len(MESES) + 1):
            if not plan[mes]:
                #No hay objetivos en este mes
                break
            
            file.write(f"\n{MESES[mes - 1]}:\n")

            for index, objetivo in enumerate(plan[mes]):
                file.write(f"[ ] {index}. {objetivo.nombre_objetivo} ({objetivo.cantidad} {objetivo.unidades}/mes). Total: {objetivo.limite}\n")

    print(f"Plan guardado exitosamente en '{fichero_path}'")



objetivos = []

while True:

    mostrar_menu()

    opcion = input("Selecciona una opcion: ")

    match opcion:
        case "1":
            if len(objetivos) >= 10:
                print("ERROR: Hay muchos objetivos cargados (Maximo 10)")
            else:
                objetivo = request_objetivo()
                objetivos.append(objetivo)
                print("¡Objetivo añadido con exito!")
        case "2":
            if len(objetivos) == 0:
                print("\nNo hay objetivos para realizarles una planificacion. Ingrese uno porfavor")
            else:
                plan = calcular_plan(objetivos)
                mostrar_plan(plan)
        case "3":
            if len(objetivos) == 0:
                print("\nNo hay planificacion para guardar. Ingrese una porfavor")
            else:
                plan = calcular_plan(objetivos)
                guardar_plan(plan)
        case "4":
            print("\nSaliendo del programa....")
            break
        case _:
            print("\nERROR: Coloque digitos validos (1-4).")