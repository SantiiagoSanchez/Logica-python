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