#El junior siempre va a tener una sola tarea, el senior siempre un numero par, el semi-senior un numero impar y el tester un numero primo

def es_primo(numero:int):
    if numero < 2:
        return False
    for i in range (2, numero):
        if(numero % i) == 0:
            return False
    return True

def repartir_Tareas(tareasTotales:int):
    
    junior = 1
    tareasTotales -= junior #Esta va a ser la tarea para un jr

    tareas_repartidas = []

    for senior in range(2, tareasTotales, 2):
        for semi_senior in range(1, tareasTotales, 2):
            tester = tareasTotales - senior - semi_senior

            if senior > 0 and es_primo(senior):
                tareas_repartidas.append({
                    "Senior": tester,
                    "Semi Senior": semi_senior,
                    "Tester": senior,
                    "Junior": junior
                })

    if tareas_repartidas:
        return tareas_repartidas

    return "No se pudo repartir las tareas"


try:
    tareas = int(input("Cuantas tareas tienes que repartir con todo tu equipo?: "))
    tareas_repartidas = repartir_Tareas(tareas)

    if isinstance(tareas_repartidas, list):
        print("Posibles distribuciones para las tareas del equipo:")
        for index, distribucion in enumerate(tareas_repartidas):
            print(f"{index + 1}. {distribucion}")
            
        print()
        print(f"Distribucion media {tareas_repartidas[int(len(tareas_repartidas) / 2)]}")
    else:
        print(tareas_repartidas)
except ValueError:
    print("ERROR: Porfavor. Se tiene que introducir numeros enteros")