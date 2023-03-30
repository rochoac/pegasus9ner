import turtle
import tkinter
import math

from tkinter import *
from tkinter import messagebox
#from tkinter import photoimage


# Formulario
ventana = tkinter.Tk()
ventana.geometry("1500x900")
ventana.title("PEGASUS 9NER")
ventana.config(background = "#213141")



# Canvas LED:
canvas = tkinter.Canvas(master = ventana, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=1, columnspan=1) # , sticky='nsew')
canvas.pack(side="right")
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")


# Variables:
	# 1
hdgSet1 = StringVar(); turnType1 = StringVar(); spd1 = StringVar()
hdgSense1 = StringVar()
sentido1 = 1

hdgSet1.set(90)
rumboOrdenado1 = StringVar()

	# 2
hdgSense2 = StringVar()
hdgSet2 = StringVar();
sentido2 = 1

hdgSet2.set(90)
rumboOrdenado2 = StringVar()

rumboOrdenado1.set("no")
rumboOrdenado2.set("no")


velocidad = 50
vel = StringVar()
anguloGiro = StringVar()
actualizar = StringVar()

# Función actualzar:

headNuevo1 = hdgSet1.get()
headAntiguo1 = 90

headNuevo2 = hdgSet2.get()
headAntiguo2 = 90

def actualizarDatos(cadena_vacia):
	global headAntiguo1
	global headNuevo1
	global sentido1
	
	global headAntiguo2
	global headNuevo2
	global sentido2
	
	if hdgSet1.get().isdigit():			# Actualiza HEADING 1
		if int(hdgSet1.get()) < 361:
			headNuevo1 = hdgSet1.get()
			if rumboOrdenado1.get() != "no":
				headAntiguo1 = rumboOrdenado1.get()
			if int(headNuevo1) != int(headAntiguo1):
				rumboOrdenado1.set( headNuevo1 )
		else:
			messagebox.showwarning(message = "Papafrita, dame un rumbo de verdad!")
	else:
		messagebox.showwarning(message = "Papafrita, dame un rumbo de verdad!")


	if hdgSet2.get().isdigit():			# Actualiza HEADING 2
		if int(hdgSet2.get()) < 361:
			headNuevo2 = hdgSet2.get()
			if rumboOrdenado2.get() != "no":
				headAntiguo2 = rumboOrdenado2.get()
			if int(headNuevo2) != int(headAntiguo2):
				rumboOrdenado2.set( headNuevo2 )
		else:
			messagebox.showwarning(message = "Papafrita, dame un rumbo de verdad!")
	else:
		messagebox.showwarning(message = "Papafrita, dame un rumbo de verdad!")
		
	
	if hdgSense1.get() == "l" or hdgSense1.get() == "L":	# Sentido giro 1
		sentido1 = -1
	else:
		sentido1 = 1
		
	if hdgSense2.get() == "l" or hdgSense2.get() == "L":	# Sentido giro 2
		sentido2 = -1
	else:
		sentido2 = 1
		

	
# Función reset:

def reset():
	global cuentaWhile
	avo1.goto(-350,-350)
	avo2.goto(-350,-340)
	avo1.clear()
	avo2.clear()
	cuentaWhile = 0
	
	hdgSet1.set("45")
	hdgSet2.set("45")
	

def velocidadAnimacion(arg):
	a = int(vel.get())
	if 0< a < 70:
		velocidad = a
		return a

		# Cuadro texto velocidad (y etiqueta):

velocidad_entry = Entry(textvariable = vel, width = "5")
velocidad_entry.place(x = 22, y = 430)
velocidad_entry.bind('<Return>', velocidadAnimacion)
vel.set(velocidad)

velocidad_label = Label(text="Velocidad de animación: 1 máx / 69 min")
velocidad_label.place(x=22, y = 400)


		# Cuadros de texto (FIGHTER):
		
srn1_entry = Entry(width = "5")
srn1_entry.place(x=110, y=47)

hdgSet1_entry = Entry(textvariable = hdgSet1, width = "5")
hdgSet1_entry.place(x = 110, y = 87)
hdgSet1_entry.bind('<Return>', actualizarDatos)

hdgSense1_entry = Entry(textvariable = hdgSense1, width = "5")
hdgSense1_entry.place(x = 110, y = 127)
hdgSense1_entry.bind('<Return>', actualizarDatos)

alt1_entry = Entry(width = "5")
alt1_entry.place(x = 110, y = 327)


		# Cuadros de texto (BANDIT):

srn2_entry = Entry(width = "5")
srn2_entry.place(x=410, y=47)

hdgSet2_entry = Entry(textvariable = hdgSet2, width = "5")
hdgSet2_entry.place(x = 410, y = 87)
hdgSet2_entry.bind('<Return>', actualizarDatos)

hdgSense2_entry = Entry(textvariable = hdgSense2, width = "5")
hdgSense2_entry.place(x = 410, y = 127)
hdgSense2_entry.bind('<Return>', actualizarDatos)

alt2_entry = Entry(width = "5", bg = "yellow")
alt2_entry.place(x = 410, y = 327)





		# Etiquetas (FIGHTER):
	 
fighter_label = Label(text="FIGHTER")
fighter_label.config(bg="blue")
fighter_label.place(x = 100, y = 10)

srn1_label = Label(text="SRN")
srn1_label.place(x=22, y=50)

hdgSet1_label = Label(text="HDG SET")
hdgSet1_label.place(x=22, y=90)

hdgSense1_label = Label(text="HDG SENSE")
hdgSense1_label.place(x=22, y=130)

turnType1_label = Label(text="TURN TYPE")
turnType1_label.place(x=22, y=170)

spdSet1_label = Label(text="SPD/SET")
spdSet1_label.place(x=22, y = 210)

spd1_label = Label(text = "SPD")
spd1_label.place(x = 22, y = 250)

altSet1_label = Label(text="ALT/SET")
altSet1_label.place(x=22, y = 290)

alt1_label = Label(text = "ALT")
alt1_label.place(x = 22, y = 330)



		# Etiquetas (BANDIT):
		
bandit_label = Label(text="BANDIT")
bandit_label.config(bg = "red")
bandit_label.place(x = 400, y = 10)

srn2_label = Label(text="SRN")
srn2_label.place(x=322, y=50)

hdgSet2_label = Label(text="HDG SET")
hdgSet2_label.place(x=322, y=90)

hdgSense2_label = Label(text="HDG SENSE")
hdgSense2_label.place(x=322, y=130)

turnType2_label = Label(text="TURN TYPE")
turnType2_label.place(x=322, y=170)

spdSet2_label = Label(text="SPD/SET")
spdSet2_label.place(x=322, y = 210)

spd2_label = Label(text = "SPD")
spd2_label.place(x = 322, y = 250)

altSet2_label = Label(text="ALT/SET")
altSet2_label.place(x= 322, y = 290)

alt2_label = Label(text = "ALT")
alt2_label.place(x = 322, y = 330)



		# Botón reset

reset_btn = Button(ventana, text = "Reset", command = reset, width = "3", height = "2	", bg = "#00CD63" )
reset_btn.place(x = 22, y = 700)


# Aviones

avo1 = turtle.RawTurtle(screen)
avo1.speed(0)
avo1.shape("circle")
avo1.color("blue")
avo1.turtlesize(0.3)
avo1.penup()  # Evita que dibuje líneas mientras se mueve
avo1.goto(0,0)
avo1.dx = 1
avo1.dy = 0



avo2 = turtle.RawTurtle(screen)
avo2.speed(0)
avo2.shape("circle")
avo2.color("red")
avo2.turtlesize(0.3)
avo2.penup()  # Evita que dibuje líneas mientras se mueve
avo2.goto(0,-30)
avo2.dx = 1
avo2.dy = 0


		# Líneas auxiliares y DELTA:

l1 = turtle.RawTurtle(screen)
l1.speed(10)
l1.shape("classic")
l1.color("yellow")
l1.turtlesize(0.1)
l1.penup()
l1.goto(-300,-300)

l2 = turtle.RawTurtle(screen)
l2.speed(10)
l2.shape("circle")
l2.color("yellow")
l2.turtlesize(0.1)
l2.penup()
l2.goto(-300,-300)

l_delta = turtle.RawTurtle(screen)
l_delta.speed(10)
l_delta.shape("circle")
l_delta.color("yellow")
l_delta.turtlesize(0.1)
l_delta.penup()
l_delta.goto(-300,-300)


		# Función líneas auxiliares:
def auxLin():
	l1.clear()
	l2.clear()
	
	d = 5.1; l = 60
	dx = avo2.dx; dy = avo2.dy
	x = avo2.xcor(); y = avo2.ycor()
	
	l1.goto(x + dy * d, y - dx * d)
	l2.goto(x - dy * d, y + dx * d)
	
	l1.pendown()
	l2.pendown()
	
	l1.goto(l1.xcor() + dx * l, l1.ycor() + dy * l)
	l2.goto(l2.xcor() + dx * l, l2.ycor() + dy * l)
	
	l1.penup()
	l2.penup()
	
	
	
		# Función líneas DELTA:

dibujadelta = 3

def deltaLin():
	global dibujadelta
	l_delta.clear()
	
	if dibujadelta % 2 > 0:
		l_delta.goto(-380, 380)
		l_delta.pendown()

		l_delta.goto(-380, -100)
		l_delta.goto(100, -380)
		l_delta.goto(380, -380)
		l_delta.goto(380, 380)
		l_delta.goto(-380, 380)
		
		l_delta.penup()
	dibujadelta = dibujadelta +1
	
	
	


		# Botón líneas auxiliares:
aux_btn = Button(ventana, text = "LADs auxiliares", command = auxLin, width = "7", height = "2	", bg = "#00CD63")
aux_btn.place(x = 22, y = 800)

		# Botón dibuja DELTA:
aux_btn = Button(ventana, text = "DELTA on/off", command = deltaLin, width = "7", height = "2	", bg = "#00CD63")
aux_btn.place(x = 300, y = 800)



		# Función BORRAR LÍNEAS AUXILIARES:
def borraLin():
	l1.clear()
	l2.clear()
	
		# Botón 	BORRA LÍNEAS AUXILIARES:
borraAux_btn = Button(ventana, text = "Borra LAD", command = borraLin, width = "7",height = "2", bg = "#00CD63")
borraAux_btn.place(x = 130, y = 800)


		# LAD T -> F:

dirTF = StringVar()

ladTF_label = Label(text = "LAD T -> F", bg = "yellow")
ladTF_label.place(x= 250, y = 650)

ladTF_entry = Entry(textvariable = dirTF, width = "5", bg = "yellow")
ladTF_entry.place(x = 350, y = 650)


		# LAD F -> T:
dirFT = StringVar()

ladFT_label = Label(text = "LAD F -> T", bg = "yellow")
ladFT_label.place(x= 250, y = 700)

ladFT_entry = Entry(textvariable = dirFT, width = "5", bg = "yellow")
ladFT_entry.place(x = 350, y = 700)

		# Distancia LAD:
distancia = StringVar()

ladDistancia_entry = Entry(textvariable = distancia, width = "5", bg = "yellow")
ladDistancia_entry.place(x = 420, y = 675)


# Main game loop

rumboInicial = 90
rumboOrdenado1.set(rumboInicial)
rumboOrdenado2.set(rumboInicial)

x_sen = 0; y_sen=0

cuentaWhile = 0
while True:
	
	ventana.update()	# Mueve la bola	
	
	avo1.setx(avo1.xcor() + avo1.dx)
	avo1.sety(avo1.ycor() + avo1.dy)
	avo1.stamp()	# Deja huella
	
	avo2.setx(avo2.xcor() + avo2.dx)
	avo2.sety(avo2.ycor() + avo2.dy)
	avo2.stamp()


	
	if cuentaWhile > 3:		# Borra huella
		avo1.clearstamps(1)
		avo2.clearstamps(1)
	
	# LADs:
	dirFT.set(str( int( (360 - (avo1.towards(avo2.xcor(), avo2.ycor()) - 90)) % 360 ) ) + "º") #  towards da rumbos (90,360,270,180) en vez de (360, 90, 180, 270)
	dirTF.set(str( int( (360 - (avo2.towards(avo1.xcor(), avo1.ycor()) - 90)) % 360 ) ) + "º")
	distancia.set(str( int( avo1.distance(avo2.xcor(), avo2.ycor()) / 10 ) )+ "NM")
	
	
	for i in range(velocidadAnimacion('null')): # Retiene la bola
		ventana.update()
		avo1.setx(avo1.xcor())
		avo1.sety(avo1.ycor())
		avo2.setx(avo2.xcor())
		avo2.sety(avo2.ycor())

# Giro 1:

	'''
	>>> (300-320)%360
	340
	>>> abs(300-320)%360
	20
	'''

	if abs(int(headAntiguo1) - int(headNuevo1)) % 360  > 15:
		headAntiguo1 = (int(headAntiguo1) +  20 * sentido1) % 360
		rumboOrdenado1.set( headAntiguo1 )
	else:
		rumboOrdenado1.set( headNuevo1 )
		
# Giro 2:

	if abs(int(headAntiguo2) - int(headNuevo2)) % 360  > 15:
		headAntiguo2 = (int(headAntiguo2) +  20 * sentido2) % 360
		rumboOrdenado2.set( headAntiguo2 )
	else:
		rumboOrdenado2.set( headNuevo2 )
		

# Rumbos:
	if (rumboOrdenado1.get() != "no"):
	
		x_sen1 = math.sin(int(rumboOrdenado1.get())*math.pi/180)
		y_cos1 = math.cos(int(rumboOrdenado1.get())*math.pi/180)
		
		avo1.dx = int(x_sen1 * 10) 
		avo1.dy = int(y_cos1 * 10)
		rumboOrdenado1.set("no")
			
	if (rumboOrdenado2.get() != "no"):
			
		x_sen2 = math.sin(int(rumboOrdenado2.get())*math.pi/180)
		y_cos2 = math.cos(int(rumboOrdenado2.get())*math.pi/180)
			
		avo2.dx = int(x_sen2 * 10) 
		avo2.dy = int(y_cos2 * 10)
		rumboOrdenado2.set("no")
	
	cuentaWhile = cuentaWhile + 1
	
# Warning:
	if -380 > avo1.xcor() or 380 < avo1.xcor() or -380 > avo1.ycor() or 380 < avo1.ycor():
		messagebox.showwarning(message = "Ahhhh, eres un acumulador de trienios!!!!")
		avo1.goto(0,0)
		avo2.goto(0,0)
	

	if -380 > avo2.xcor() or 380 < avo2.xcor() or -380 > avo2.ycor() or 380 < avo2.ycor():
		messagebox.showwarning(message = "Ahhhh, eres un acumulador de trienios!!!!")
		avo1.goto(0,0)
		avo2.goto(0,0)
