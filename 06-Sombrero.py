import random

casas = {
    "Visual": 0,
    "Auditivo": 0,
    "Kinestésico": 0,
    "Lectura/Escritura": 0
}

preguntas = [
    {
        "Pregunta" : "Cuando tienes que estudiar un tema nuevo, ¿qué prefieres hacer?",
        "Respuestas" : [
            {"opcion": "Practicar haciendo ejercicios relacionados con el tema", "casa": "Kinestésico"},
            {"opcion": "Leer un libro o artículo sobre el tema", "casa": "Lectura/Escritura"},
            {"opcion": "Ver un video explicativo o una infografía", "casa": "Visual"},
            {"opcion": "Escuchar una charla o un podcast sobre el tema", "casa": "Auditivo"}
        ]
    },
    {
        "Pregunta" : "¿Cómo prefieres recibir instrucciones para realizar una tarea?",
        "Respuestas" : [
            {"opcion": "En una lista escrita o un manual paso a paso", "casa": "Lectura/Escritura"},
            {"opcion": "A través de una presentación visual (diagrama, diapositivas)", "casa": "Visual"},
            {"opcion": "Recibiendo demostraciones prácticas o instrucciones en acción", "casa": "Kinestésico"},
            {"opcion": "Explicadas verbalmente por alguien", "casa": "Auditivo"}
        ]
    },
    {
        "Pregunta" : "Cuando necesitas recordar algo importante, ¿cómo lo haces?",
        "Respuestas" : [
            {"opcion": "Escribo notas o resúmenes para recordarlo", "casa": "Lectura/Escritura"},
            {"opcion": "Lo relaciono con una acción que puedo hacer", "casa": "Kinestésico"},
            {"opcion": "Repito lo que escuché en voz alta o me grabo", "casa": "Auditivo"},
            {"opcion": "Visualizo una imagen o un gráfico relacionado", "casa": "Visual"}
        ]
    },
    {
        "Pregunta" : "Si estás aprendiendo algo nuevo, ¿qué te ayuda más?",
        "Respuestas" : [
            {"opcion": "Leer sobre el tema en un libro o artículo", "casa": "Lectura/Escritura"},
            {"opcion": "Escuchar explicaciones detalladas o podcasts", "casa": "Auditivo"},
            {"opcion": "Ver ilustraciones, diagramas o videos relacionados", "casa": "Visual"},
            {"opcion": "Hacer ejercicios prácticos o experimentos para entenderlo", "casa": "Kinestésico"}
        ]
    },
    {
        "Pregunta" : "Cuando participas en una clase o reunión, ¿qué tipo de material prefieres?",
        "Respuestas" : [
            {"opcion": "Escuchar una charla o debate sobre el tema", "casa": "Auditivo"},
            {"opcion": "Gráficos, diagramas o presentaciones visuales", "casa": "Visual"},
            {"opcion": "Participar en actividades prácticas o demostraciones", "casa": "Kinestésico"},
            {"opcion": "Leer notas o resúmenes escritos del tema", "casa": "Lectura/Escritura"}
        ]
    },
    {
        "Pregunta" : "¿Cómo prefieres resolver problemas nuevos?",
        "Respuestas" : [
            {"opcion": "Escuchando a alguien que explique cómo resolverlo", "casa": "Auditivo"},
            {"opcion": "Haciendo pruebas o experimentos prácticos", "casa": "Kinestésico"},
            {"opcion": "Mirando ejemplos visuales o diagramas que me guíen", "casa": "Visual"},
            {"opcion": "Leyendo sobre el problema y buscando soluciones escritas", "casa": "Lectura/Escritura"}
        ]
    },
    {
        "Pregunta" : "Cuando estás aprendiendo algo complejo, ¿cómo prefieres que te lo enseñen?",
        "Respuestas" : [
            {"opcion": "Con demostraciones prácticas y actividades relacionadas", "casa": "Kinestésico"},
            {"opcion": "Con ejemplos visuales, gráficos o mapas mentales", "casa": "Visual"},
            {"opcion": "Con un texto escrito, manual o guía detallada", "casa": "Lectura/Escritura"},
            {"opcion": "Con una explicación verbal o discusión sobre el tema", "casa": "Auditivo"}
        ]
    },
    {
        "Pregunta" : "Cuando tienes que estudiar para un examen, ¿cómo prefieres hacerlo?",
        "Respuestas" : [
            {"opcion": "Leyendo y escribiendo notas de los temas a estudiar", "casa": "Lectura/Escritura"},
            {"opcion": "Escuchando explicaciones grabadas o repitiendo en voz alta", "casa": "Auditivo"},
            {"opcion": "Viéndolo todo visualmente en diagramas y gráficos", "casa": "Visual"},
            {"opcion": "Haciendo pruebas prácticas o simulaciones", "casa": "Kinestésico"}
        ]
    },
    {
        "Pregunta" : "Si tienes que aprender a usar una nueva herramienta o tecnología, ¿cómo lo haces?",
        "Respuestas" : [
            {"opcion": "Mirando videos tutoriales o ejemplos visuales", "casa": "Visual"},
            {"opcion": "Probando la herramienta directamente y experimentando con ella", "casa": "Kinestésico"},
            {"opcion": "Leyendo el manual o la guía escrita para entender cómo funciona", "casa": "Lectura/Escritura"},
            {"opcion": "Escuchando un tutorial en audio o buscando instrucciones verbales", "casa": "Auditivo"}
        ]
    },
    {
        "Pregunta" : "¿Qué prefieres hacer en tu tiempo libre para aprender algo nuevo?",
        "Respuestas" : [
            {"opcion": "Escuchar podcast o conferencias sobre el tema", "casa": "Auditivo"},
            {"opcion": "Participar en actividades prácticas o talleres", "casa": "Kinestésico"},
            {"opcion": "Leer artículos o libros que hablen sobre el tema", "casa": "Lectura/Escritura"},
            {"opcion": "Ver tutoriales o documentales relacionados con el tema", "casa": "Visual"}
        ]
    }
]

print("\n¡Bienvenido al test de estilos de aprendizaje!")
print("El sombrero seleccionador decidira cual es tu casa de aprendizaje.")

nombre = input("\n¿Cual es tu nombre? ")

for index, pregunta in enumerate(preguntas):
    print(f"\nPregunta N° {index + 1}: {pregunta["Pregunta"]}")

    for i, respuesta in enumerate(pregunta["Respuestas"]):
        print(f"{i + 1}. {respuesta["opcion"]}")
    
    seleccion = int(input("Selecciona la respuesta entre 1 y 4: "))

    respuesta_seleccionada = pregunta["Respuestas"][seleccion - 1]
    casas[respuesta_seleccionada["casa"]] += 1

    casa_ganadora = max(casas, key=casas.get)
    resultados = list(casas.values())

if resultados.count(max(resultados)) > 1:
    casas_empatadas = [
        casa for casa, puntos in casas.items() if puntos == max(resultados)
    ]

    casa_ganadora = random.choice(casas_empatadas)

    print(f"\nLa desicion fue muy complicada {nombre}, pero lo tengo. Tu casa de aprendizaje es {casa_ganadora}")
    print(f"Estos fueron los resultados: {casas}")


else:
    print(f"\nMuy bien {nombre}, tu casa de aprendizaje es {casa_ganadora}")
    print(f"Estos fueron los resultados: {casas}")
