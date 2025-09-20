import turtle as t

# Crear un cuadrado
cuadrado = t.Turtle()
cuadrado.shape("square")
cuadrado.color("blue")
cuadrado.fillcolor("white")
cuadrado.shapesize(2)
cuadrado.penup()  # Para que no deje línea al moverse
cuadrado.speed(3)

# Funciones de movimiento
def mover_arriba():
    y = cuadrado.ycor()
    cuadrado.sety(y + 20)

def mover_abajo():
    y = cuadrado.ycor()
    cuadrado.sety(y - 20)

def mover_izquierda():
    x = cuadrado.xcor()
    cuadrado.setx(x - 20)

def mover_derecha():
    x = cuadrado.xcor()
    cuadrado.setx(x + 20)


# Controles del teclado
t.listen()
t.onkey(mover_arriba, "Up")
t.onkey(mover_abajo, "Down")
t.onkey(mover_izquierda, "Left")
t.onkey(mover_derecha, "Right")

# Mantener la ventana abierta
t.done()
