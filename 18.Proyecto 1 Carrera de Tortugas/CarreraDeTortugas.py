import turtle
import random

#Pantalla
s = turtle.Screen()
s.title("Carrera de Tortugas")
s.bgcolor("salmon")

#Tortugas

jugador1 = turtle.Turtle()
jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("purple")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2 = turtle.Turtle()
jugador2.hideturtle()
jugador2.color("blue")
jugador2.shape("turtle")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

#Dibujar casas
jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

#Mover tortugas a punto de partida
jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(-250,-175)
jugador2.showturtle()

#dado
dado = [1,2,3,4,5,6]

#Juego
for i in range(20):
    if jugador1.pos() >= (200,200):
        print("¡¡La tortuga morada ha ganado!!")
        break
    elif jugador2.pos() >= (200,-200):
        print("¡¡La tortuga azul ha ganado!!")
        break
    else:
        turno1 = input("Presiona Enter para mover a la tortuga morada")
        turno1 = random.choice(dado)
        print("Tu número es: ", turno1,"\nAvanzas: ", turno1*20)
        jugador1.pendown()
        jugador1.forward(turno1*20)

        
        turno2 = input("Presiona Enter para mover a la tortuga azul")
        turno2 = random.choice(dado)
        print("Tu número es: ", turno2,"\nAvanzas: ", turno2*20)
        jugador2.pendown()
        jugador2.forward(turno2*20)


turtle.done()