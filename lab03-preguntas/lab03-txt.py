import os

path = os.path.join("arcade-labs", "lab03-preguntas", "preguntas.txt")

def extraer_pregunta(pregunta: str) -> dict:
    pregunta_dict = {}
    pregunta_respuestas = pregunta.split("|")
    pregunta_dict["pregunta"] = pregunta_respuestas[0]
    pregunta_dict["correcta"] = pregunta_respuestas[1]
    pregunta_dict["opciones"] = pregunta_respuestas[1:] 
    return pregunta_dict

def juego_preguntas(preguntas: list):
    opciones = ["a)", "b)", "c)", "d)"]
    puntos = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for i in range(len(pregunta["opciones"])):
            print(f"{opciones[i]} {pregunta["opciones"][i]}")
            scan = input("Seleccione la respuesta correcta: ")
            if scan == pregunta["correcta"]:
                puntos += 5

with open(path, "r") as file:
    preguntas = []
    for line in file:
        print(line.strip())
        line = extraer_pregunta(line.strip())
        print(line)
        preguntas.append(line)