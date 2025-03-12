import random

class Participantes:
    def __init__(self, nombre, pais) -> None:
        self.nombre = nombre
        self.pais = pais
    def __eq__(self, otro):     #Metodo auxiliar para saber si es correcto lo que puso el usuario o no
        if isinstance(otro, Participantes):
            return self.nombre == otro.nombre and self.pais == otro.pais
        return False
    def __hash__(self):
        return hash(self.nombre, self.pais)




class Olimpiadas:

    def __init__(self):
        self.eventos = []
        self.participantes = {}
        self.resultados_eventos = {}
        self.resultados_pais = {}


#-------------------------REGISTRAR EVENTOS------------------------
    def register_eventos(self):
        evento = input("Introduce el nombre del evento deportivo: ").strip()
        
        if evento in self.eventos:
            print(f"El evento {evento} ya esta registrado")
        else:
            self.eventos.append(evento)
            print(f"El evento {evento} se registro correctamente.")

#-------------------------REGISTRAR PARTICIPANTES------------------------
    def register_participantes(self):

        if not self.eventos:
            print("No hay eventos registrados. Primero registra uno")
            return
        

        nombre = input("Introduce el nombre del participante: ").strip()
        pais = input("Introduce el pais del participante: ").strip()
        participante = Participantes(nombre, pais)

        print("Eventos deportivos disponibles:")
        for index, evento in enumerate(self.eventos):
            print(f"{index + 1}. {evento}")

        evento_elegido = int(input("Selecciona el numero del evento para asignar al participante: ")) - 1

        if evento_elegido >= 0 and evento_elegido < len(self.eventos):
            evento = self.eventos[evento_elegido]

            if evento in self.participantes and participante in self.participantes[evento]:
                print(f"ERROR: El participante {nombre} de {pais} ya esta registrado en {evento}")
            else:
                if not evento in self.participantes:
                    self.participantes[evento] = []

                self.participantes[evento].append(participante)
                print(f"El participante {nombre} de {pais} se añadio correctamente a {evento}")
        else:
            print("ERROR: Seleccion de deporte invalido. No se registro el participante")
#-------------------------SIMULAR EVENTOS------------------------
    def simulate_eventos(self):
        if not self.eventos:
            print("No hay eventos registrados para simular. Registra uno primero")
            return

        for evento in self.eventos:
            if len(self.participantes[evento]) < 3:
                print(f"No hay suficientes participantes para simular el evento {evento}, minimo 3.")
                continue

            podio_evento = random.sample(self.participantes[evento], 3) #Esto me trae 3 participantes random de el evento
            random.shuffle(podio_evento) #Esto es para ordenar el podio de una manera aleatoria

            oro, plata, bronce = podio_evento
            # esto es como poner:
            # oro = podio_evento[0]
            # plata = podio_evento[1]
            # bronce = podio_evento[2]

            self.resultados_eventos[evento] = [oro, plata, bronce]
            self.update_resultados_paises(oro.pais, "oro")
            self.update_resultados_paises(plata.pais, "plata")
            self.update_resultados_paises(bronce.pais, "bronce")

            print(f"Resultados de la simulacion del evento de {evento}")
            print(f"Oro: {oro.nombre} ({oro.pais})")
            print(f"Plata: {plata.nombre} ({plata.pais})")
            print(f"Bronce: {bronce.nombre} ({bronce.pais})")
#-------------------------SUMAR MEDALLAS POR PAIS------------------------

    def update_resultados_paises(self, pais, medalla):
        if not pais in self.resultados_pais: #Si no hay pais, lo creo con las medallas en 0
            self.resultados_pais[pais] = {"oro": 0, "plata": 0, "bronce": 0}
        self.resultados_pais[pais][medalla] += 1
#-------------------------CREAR INFORMES------------------------

    def create_reportes(self):
        print("Informes de los juegos olimpicos")
        if self.resultados_eventos:
            print("Informes de participantes del evento")
            for evento, ganadores in self.resultados_eventos.items():
                print(f"Evento: {evento}")
                print(f"Oro: {ganadores[0].nombre} ({ganadores[0].pais})")
                print(f"Plata: {ganadores[1].nombre} ({ganadores[1].pais})")
                print(f"Bronce: {ganadores[2].nombre} ({ganadores[2].pais})")
        else:
            print("ERROR: No hay resultados de eventos")

        if self.resultados_pais:
            print("Informes de medallas de paises")
            for pais, medalla in sorted(self.resultados_pais.items(), key=lambda x: (x[1]["oro"], x[1]["plata"], x[1]["bronce"]), reverse= True):
                print(f"{pais}: Oro {medalla['oro']}, Plata {medalla['plata']}, Bronce {medalla['bronce']}")

        else:
            print("ERROR: No hay medallas por pais registradas")


olimpiadas = Olimpiadas()


print("SIMULADOR DE JUEGOS OLIMPICOS")

while True:
    print()
    print("1. Registro de eventos")
    print("2. Registro de participantes")
    print("3. Simulacion de eventos")
    print("4. Creacion de informes")
    print("5. Salir")

    option = input("Selecciona una opcion:")

    match option:
        case "1":
            olimpiadas.register_eventos()
        case "2":
            olimpiadas.register_participantes()
        case "3":
            olimpiadas.simulate_eventos()
        case "4":
            olimpiadas.create_reportes()
        case "5":
            print("Saliendo del simulador")
            break
        case _:
            print("Opcion invalida, selecciona una opcion valida")