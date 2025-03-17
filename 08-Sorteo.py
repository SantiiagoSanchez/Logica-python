import csv
import os
import random

def leer_csv() -> list:
    file_direction = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_direction}/subs.csv"

    data = []

    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "activo":
                data.append(row)

    return data

def elegir_ganadores(data: list):
    if len(data) < 3:
        raise ValueError("No hay suficientes participantes para realizar el sorteo")
    return random.sample(data, 3)

def mostrar_ganadores(ganadores):
    regalos = ["Remera de Futbol", "Pelota de Futbol", "Botines"]
    for ganador, regalos in zip(ganadores, regalos):
        print(f"{regalos}: {ganador["email"]} (Id: {ganador["id"]})")


try:
    data = leer_csv()
    ganadores = elegir_ganadores(data)
    mostrar_ganadores(ganadores)
except Exception as e:
    print(e)
