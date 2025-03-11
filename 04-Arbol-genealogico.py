class Persona:

    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.pareja = None
        self.hijos = []
        self.tienesPadres = False

    def post_pareja(self, pareja):
        if self.pareja is not None:
            print(f"{self.nombre} ya tiene pareja. ({self.pareja.nombre})")
        else:
            self.pareja = pareja
            print(f"{self.nombre} es pareja de {self.pareja}.")

    def post_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
            print(f"{self.nombre} a tenido un hijo: {hijo.nombre}")
        else:
            print(f"{hijo.nombre} ya es hijo de {self.nombre}")

class ArbolFamiliar:

    def __init__(self):
        self.gente = {}

    def post_persona(self, id, nombre):
        if id in self.gente:
            print(f"Ya existe una persona con el id {id}")
        else:
            persona = Persona(id, nombre)
            self.gente[id] = persona
            print(f"La persona con nombre {nombre} se añadio correctamente al arbol con el id: {id}")

    def delete_persona(self, id):
        persona = self.gente[id]
        if id in self.gente:
            del self.gente[id]
            print(f"Se ha eliminado {persona.nombre} con el id {id}")
        else:
            print(f"No existe una persona con el id {id}")

    def set_pareja(self, id1, id2):
        if id1 in self.gente and id2 in self.gente:
            persona1 = self.gente[id1]
            persona2 = self.gente[id2]
            persona1.post_pareja(persona2)
        else:
            print(f"Algun id no es correcto")

    def set_hijo(self, padre_id, hijo_id):

        if padre_id in self.gente and hijo_id in self.gente:
            if padre_id == hijo_id:
                print("Los IDs no pueden ser iguales a la hora de asignar un hijo")
            else:
                padre = self.gente[padre_id]
                if padre.pareja is None:
                    print(f"Se necesita una pareja para tener un hijo")
                else:
                    hijo = self.gente[hijo_id]
                    if hijo.tienesPadres:
                        print(f"{hijo.name} (ID: {id}) ya tiene padres")
                    else:
                        hijo.tienesPadres = True
                        padre.post_hijo(hijo)
                        padre.pareja.post_hijo(hijo)
        else:
            print("Algun id no es correcto")

    def get_arbol(self):

        visitado = set()
        def print_person(person, nivel = 0):

            if person.id in visitado:
                return
            
            visitado.add(person.id)

            indent = "\t" * nivel

            print(f"{indent} - {person.nombre} (ID: {person.id})")

            if person.pareja:
                visitado.add(person.pareja.id)
                print(f"{indent} - Pareja: {person.pareja.nombre} - (ID: {person.id})")

            if person.hijos:
                print(f"{indent} Hijos:")
                for hijo in person.hijos:
                    print_person(hijo, nivel + 1)


        for person in self.gente.values():
            es_hijo = person.tienesPadres
            if not es_hijo:
                print_person(person)

arbol = ArbolFamiliar()

arbol.post_persona(1, "Abuelo")
arbol.post_persona(2, "Abuela")
arbol.post_persona(3, "Padre")
arbol.post_persona(4, "Madre")
arbol.post_persona(5, "Hijo")
arbol.post_persona(6, "Hija")


arbol.set_pareja(1, 2)

arbol.set_hijo(1, 3)
arbol.set_hijo(2, 3)

arbol.set_pareja(3, 4)

arbol.set_hijo(3, 5)
arbol.set_hijo(4, 5)
arbol.set_hijo(3, 6)
arbol.set_hijo(4, 6)

arbol.get_arbol()