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
    opciones = ["a", "b", "c", "d"]
    puntos = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for i in range(len(pregunta["opciones"])):
            print(f"{opciones[i]}) {pregunta["opciones"][i]}")

        scan = input("Seleccione la respuesta correcta: ")
        for i in opciones:
            if scan == i:
                scan = pregunta["opciones"][opciones.index(i)]
                break
        if scan == pregunta["correcta"]:
            puntos += 5
            print("¡Respuesta correcta!")
        else:
            print("Respuesta incorrecta.")

    if puntos >= 15:
        print(f"Enhorabuena, has obtenido {puntos} puntos")
    else:
        print(f"Vaya, tu puntuación ha sido de {puntos} puntos")


if __name__ == "__main__":
    with open(path, "r", encoding="utf-8") as file:
        preguntas = []
        for line in file:
            print(line.strip())
            line = extraer_pregunta(line.strip())
            print(line)
            preguntas.append(line)

        juego_preguntas(preguntas)