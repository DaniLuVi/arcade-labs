import os
import json

path = os.path.join("arcade-labs", "lab03-preguntas", "preguntas.json")

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
    with open(path, "r") as file:
        preguntas = json.load(file)

        juego_preguntas(preguntas)