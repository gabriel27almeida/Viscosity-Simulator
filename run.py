from Experiment import *

# Window

WIDTH = 500
HEIGHT = 600
scale = 20 # 1 cm = 20 px

window = Tk()
window.title("Viscosity simulation")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

E = Experiment(
	window,
	canvas,
	(WIDTH, HEIGHT),
	scale, 
	(7000, 1260, 11.10) # ball density, fluid density, fluid viscosity (SI)
)

# User input

ok = False
while not ok:
	print("Raio da esfera (5 a 10 mm): ", end="")
	radius = float(input())
	ok = (radius >= 5 and radius <= 10)

print("Altura primeira marca (cm): ", end="")
h1 = float(input())

print("Altura segunda marca (cm): ", end="")
h2 = float(input())


E.AddMarker(h1)
E.AddMarker(h2)

E.AddBall(radius/10.)

E.Run(0.0001)

window.mainloop()
