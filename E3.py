import turtle
#Funcion Recursiva

def recorrido_recursivo(tortuga, espacio, huella):
    if huella>0:
        tortuga.stamp()
        espacio = espacio +3
        tortuga.forward(espacio)
        tortuga.right(24)
        recorrido_recursivo(tortuga, espacio, huella-1)

"""ap = argparser.ArgumentParser()
ap.add_argument("--huella",required=True, help="numero de huellas")
args = vars(ap.parse_args())
huellas = int(args["huellas"])"""

#Esto es para hacer que se ejecute p[or linea de comandos con (-- huellas #detortugas)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tortuga")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
recorrido_recursivo(tess, 20, 30)

wn.mainloop()