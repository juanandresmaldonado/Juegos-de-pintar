"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

n = 0 #Variable para contar el numero de taps

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(8)) * 2 #Ajustamos a 4x4, dando 8 numeros aleatorios
state = {'mark': None}
hide = [True] * 16 #Ajustamos a 4x4 dando un maximo de 16


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100) #Ajustamos a 4x4 cambiando el 50
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 100 + ((y + 200) // 100) * 4) #Ajustamos a 4x4 Cambiando 8 y 50

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200 #Ajustamos a 4x4 Cambiando 8 y 50


def tap(x, y):
    global n
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    n = n + 1 #Actualizar el numero de taps


def draw():
    global n
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16): #Ajustamos 4x4 cambiando el 64
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    write(n, font=('Arial', 10, 'normal'))  #Imprimir el numero de taps
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()