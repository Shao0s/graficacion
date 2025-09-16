# 🐢 Proyecto de Dibujo con Turtle en Python

Este proyecto utiliza la biblioteca gráfica `turtle` de Python para dibujar formas geométricas simples: cuadrados, triángulos, círculos y líneas. Es ideal para quienes están comenzando a aprender programación visual en Python.

## 🚀 ¿Qué hace este programa?

El programa define funciones para dibujar:

- 🔷 Un **cuadrado** de color azul.
- 🔺 Un **triángulo** verde en una posición específica.
- 🔴 Un **círculo** rojo centrado en la pantalla.
- ➖ Una **línea recta** negra entre dos puntos.

Todo esto se dibuja con movimientos precisos de la "tortuga", un cursor que va dejando un trazo en la ventana gráfica.

## 📁 Estructura del código

El archivo principal define las siguientes funciones:

- `teleport(x, y)`: Mueve la tortuga sin dibujar.
- `dibujar_cuadrado(lado, color)`: Dibuja un cuadrado desde la posición actual.
- `dibujar_triangulo(x, y, lado, color)`: Dibuja un triángulo equilátero.
- `dibujar_circulo(x, y, radio, color)`: Dibuja un círculo centrado en `(x, y)`.
- `dibujar_linea(x1, y1, x2, y2, color)`: Dibuja una línea entre dos puntos.

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener **Python 3.x** instalado.
2. Ejecuta el archivo en cualquier entorno compatible (IDLE, VS Code, PyCharm, etc.):

```bash
python nombre_del_archivo.py
