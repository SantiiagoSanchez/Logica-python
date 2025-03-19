import random

class Luchador:
    def __init__(self, nombre: str, velocidad: int, ataque: int, defensa: int):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.vida = 100  #Inicializo todos los luchadores con 100 de vida. No hace falta pasarlo como parametro

    def reset_vida(self):
        self.vida = 100

    def sigue_vivo(self) -> bool:
        return self.vida > 0

    def recibir_daño(self, dano: int):

        dano_recibido = 0

        if random.random() < 0.2:
            print(f"{self.nombre} ha esquivado el ataque")
        else:
            if self.defensa >= dano:
                dano_recibido = dano * 0.1   #Esto es si la defensa es mayor que el ataque, solo recibe un 10% del ataque. 
            else:
                dano_recibido = dano - self.defensa

        self.vida = max(self.vida - dano_recibido, 0)
        print(f"{self.nombre} ha recibido {dano_recibido} de daño")
        print(f"Salud restante de {self.nombre}: {self.vida}\n")
        

class Batalla:
    def __init__(self, luchador_uno: Luchador, luchador_dos: Luchador):
        self.luchador_uno = luchador_uno
        self.luchador_dos = luchador_dos

    def pelea(self) -> Luchador:
        print(f"\n=== {self.luchador_uno.nombre} vs {self.luchador_dos.nombre} ===")

        while self.luchador_uno.sigue_vivo() and self.luchador_dos.sigue_vivo():

            if self.luchador_uno.velocidad > self.luchador_dos.velocidad:
                self.turno(self.luchador_uno, self.luchador_dos)
                if self.luchador_dos.sigue_vivo():
                    self.turno(self.luchador_dos, self.luchador_uno)
            else:
                self.turno(self.luchador_dos, self.luchador_uno)
                if self.luchador_uno.sigue_vivo():
                    self.turno(self.luchador_uno, self.luchador_dos)

        if self.luchador_uno.sigue_vivo():
            print(f"El luchador: {self.luchador_uno.nombre} ha ganado el combate")
            return self.luchador_uno
        else:
            print(f"El luchador: {self.luchador_dos.nombre} ha ganado el combate")
            return self.luchador_dos
        
    def turno(self, atacante: Luchador, defensor: Luchador):
        print(f"\n{atacante.nombre} ataca a {defensor.nombre}")
        defensor.recibir_daño(atacante.ataque)

class Torneo:
    def __init__(self, luchadores: list):
        if not self.es_potencia_de_dos(len(luchadores)):
            raise ValueError("El numero de luchadores tiene que ser potencia de 2")
        self.luchadores = luchadores

    def iniciar(self):

        ronda = 1
        while len(self.luchadores) > 1:
            print(f"\n=== Ronda N°: {ronda} ===")

            random.shuffle(self.luchadores)

            ganadores = []

            for index in range(0, len(self.luchadores), 2):
                luchador_uno = self.luchadores[index]
                luchador_dos = self.luchadores[index + 1]

                versus = Batalla(luchador_uno, luchador_dos)
                ganador = versus.pelea()
                ganadores.append(ganador)

            self.luchadores = ganadores
            ronda += 1

        print(f"\nEl ganador del torneo es {self.luchadores[0].nombre}!!")

    def es_potencia_de_dos(self, number) -> bool:
        if number <= 0:
            return False
        while number % 2 == 0:
            number //= 2
        return number == 1



luchadores = [
    Luchador("Goku", 90, 95, 80),
    Luchador("Vegeta", 85, 95, 82),
    Luchador("Gohan", 92, 85, 85),
    Luchador("Trunks", 80, 80, 75),
    Luchador("Freezer", 80, 90, 85),
    Luchador("Cell", 95, 80, 85),
    Luchador("Majin Buu", 50, 80, 85),
    Luchador("Broly", 95, 95, 95)
]


torneito = Torneo(luchadores)
torneito.iniciar()