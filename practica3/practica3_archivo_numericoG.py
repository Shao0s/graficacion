import turtle

def leer_archivos():
    filename = "matriz.txt"
    matriz = []
    with open(filename, "r") as f:
        for line in f:
            fila = line.strip().split()
            fila = [int(x) for x in fila]   # convertir a números
            matriz.append(fila)
    return matriz

#dibujar un pixel
def dibujar_pixel(x, y, color, pixel=20):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(pixel)
        turtle.right(90)
    turtle.end_fill()

# lista de Colores
colores = {
    0: "white",
    1: "black",
    2: "red",
    3: "green",
    4: "blue",
    5: "yellow",
    6: "brown",
    7: "pink",
    8: "orange",
    9: "purple"
}

matriz = leer_archivos()

turtle.speed(0)
turtle.hideturtle()
turtle.tracer(False)

pixel = 10
filas = len(matriz)
columnas = len(matriz[0])

# Calcular punto inicial
inicio_x = -columnas * pixel // 2
inicio_y = filas * pixel // 2

# Recorrer la matriz y pintar cada número
for i, fila in enumerate(matriz):
    for j, valor in enumerate(fila):
        x = inicio_x + j * pixel
        y = inicio_y - i * pixel
        color = colores.get(valor, "gray")  # gris si no está definido

        dibujar_pixel(x, y, color, pixel)

turtle.update()
turtle.done()
turt  
