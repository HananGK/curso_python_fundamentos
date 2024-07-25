import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

#pantalla
s = turtle.Screen()
s.setup(650, 650)
s.title("La Culebrita")
s.bgcolor("lightgreen")

#serpiente
serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("circle")
serpiente.penup()
serpiente.home()
serpiente.direction = "stop" #cuando se reinicia la serpiente se queda en el inicio
serpiente.color("orange")

#comida
comida = turtle.Turtle()
comida.color("blue")
comida.shape("square")
comida.penup()
comida.goto(0, 100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0   Marcador más alto: 0", align="center", font=("verdana", 24, "normal"))   

def arriba():
    serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"

def izquierda():
    serpiente.direction = "left"

def derecha():
    serpiente.direction = "right"

def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor() #muestra solo la coordenada y
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor() 
        serpiente.sety(y - 20)
    if serpiente.direction == "left":
        x = serpiente.xcor() 
        serpiente.setx(x - 20)
    if serpiente.direction == "right":
        x = serpiente.xcor() 
        serpiente.setx(x + 20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(izquierda, "Left")
s.onkeypress(derecha, "Right")

while True:
    s.update()

    if serpiente.xcor()>300 or serpiente.xcor()<-300 or serpiente.ycor()<-300 or serpiente.ycor()>300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()
        
        marcador = 0
        texto.clear()
        texto.write("Marcador: {}\tMarcador más alto: {}".format(marcador, marcador_alto), align="center", font=("verdana", 24, "normal"))


    if serpiente.distance(comida)<20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x, y)

        nuevoCuerpo = turtle.Turtle()
        nuevoCuerpo.color("orange")
        nuevoCuerpo.shape("circle")
        nuevoCuerpo.penup()
        nuevoCuerpo.goto(0, 0)
        nuevoCuerpo.speed(0)
        cuerpo.append(nuevoCuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador: {}\tMarcador más alto: {}".format(marcador, marcador_alto), align="center", font=("verdana", 24, "normal"))


    total = len(cuerpo)
    for index in range(total -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total>0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"

    time.sleep(retraso)


turtle.done()