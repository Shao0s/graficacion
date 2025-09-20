import turtle as t

# Función para mover sin dibujar
def teleport(x:float,y:float):
    t.penup()  # Levanta el lápiz
    t.setx(x)  # Va a la posición
    t.sety(y)
    t.pendown()  # Baja el lápiz

# Función para dibujar un cuadrado
def dibujar_cuadrado(lado, color):
    t.color(color)

    for _ in range(4):
        t.forward(lado)
        t.right(90)

# Función para dibujar un triángulo
def dibujar_triangulo(x, y, lado, color):
    teleport(x, y)
    t.color(color)

    for _ in range(3):
        t.forward(lado)
        t.left(120)

# Función para dibujar un círculo
def dibujar_circulo(x, y, radio, color):
    teleport(x, y - radio)  # Ajustamos para centrar el círculo
    t.color(color)
    t.circle(radio)

# Función para dibujar una línea
def dibujar_linea(x1, y1, x2, y2, color):
    teleport(x1, y1)
    t.color(color)
    t.goto(x2, y2)

# Programa principal
t.speed(3)  # Velocidad media

dibujar_cuadrado( 100, "blue")
dibujar_triangulo(-200, -100, 100, "green")
dibujar_circulo(250, -50, 50, "red")
dibujar_linea(-200, -200, 200, -200, "black")

t.done()
