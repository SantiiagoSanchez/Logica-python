#Este primer ejercicio es para saber que dia cae los sabados de la 3er semana de septiembre
from datetime import datetime, timedelta

anio_creacion = 1939
anio_aniversario = anio_creacion + 86

batman_day_aniversario_datos = []

while anio_aniversario <= anio_creacion + 100:

    septiembre = datetime(anio_aniversario, 9, 1)
    primer_sabado = 5 - septiembre.weekday() if septiembre.weekday() <= 5 else 12 - septiembre.weekday()

    tercer_sabado = septiembre + timedelta(days=primer_sabado + 14)

    batman_day_aniversario_datos.append(
        (
            anio_aniversario,
            anio_aniversario - anio_creacion,
            tercer_sabado.strftime("%d/%m/%Y")
        )
    )
    
    anio_aniversario += 1

for anio, aniversario, batman_day in batman_day_aniversario_datos:
    print(f"BATMAN DAY {anio}. (Aniversario N°: {aniversario}): {batman_day}")

#Reto 2

def sumar_zona_grid_alertas(sensors, center_x, center_y) -> int:
    total = 0

    for x in range(center_x - 1, center_x + 2):
        for y in range(center_y - 1, center_y + 2):
            for sensor in sensors:
                if sensor[0] == x and sensor[1] == y:
                    total += sensor[2]

    return total




def sistema_seguridad(sensores):

    alerta_max = 0
    alerta_max_cordenada = (0, 0)

    for x in range(1,19):
        for y in range(1,19):
            nivel_alertas = sumar_zona_grid_alertas(sensores, x, y)
            if alerta_max < nivel_alertas:
                alerta_max = nivel_alertas
                alerta_max_cordenada = (x, y)

    distancia = abs(alerta_max_cordenada[0]) + abs(alerta_max_cordenada[1])
    activar_protocolo = alerta_max > 20


    return alerta_max_cordenada, alerta_max, distancia, activar_protocolo

sensores = [
    (2, 3, 7),
    (4, 3, 8),
    (2, 2, 7),
    (10, 12, 8),
    (15, 18, 4)
]

resultado = sistema_seguridad(sensores)

print(f"Centro de cuadricula mas amenazada: {resultado[0]}.")
print(f"Maximo nivel de alerta: {resultado[1]}.")
print(f"Distancia a la BatiCueva: {resultado[2]}.")
print(f"Activar protocolo de seguridad?: {"Si" if resultado[3] else "No"}.")