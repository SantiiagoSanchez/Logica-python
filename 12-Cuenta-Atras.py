import datetime
import time
import os

hora_local = datetime.datetime(2025, 5, 31, 00, 00, 00)  #Aca se indica la hora a la que queres hacerle la cuenta atras
hora_local = hora_local.replace(tzinfo=datetime.datetime.now().astimezone().tzinfo)

fecha_utc = hora_local.astimezone(datetime.timezone.utc)

while True:

    fecha_actual = datetime.datetime.now(datetime.timezone.utc)

    cuenta_atras = fecha_utc - fecha_actual

    if cuenta_atras.total_seconds() <= 0:
        print("\nLa cuenta atras ha terminado")
        break

    dias, segundos = divmod(cuenta_atras.total_seconds(), 86400)  #Segundos por dia
    horas, segundos = divmod(segundos, 3600)
    minutos, segundos = divmod(segundos, 60)

    os.system("cls")

    print(f"Tiempo restante:\nDIAS: {int(dias)}\nHORAS: {int(horas)}\nMINUTOS: {int(minutos)}\nSEGUNDOS: {int(segundos)}")
    time.sleep(1)

