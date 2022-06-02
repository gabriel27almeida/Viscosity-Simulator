from Experiment import *

# Window

WIDTH = 500
HEIGHT = 600
scale = 100 # 1 cm = 100 px

window = Tk()
window.title("Simulador de viscosidade")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# welcome message
print("")
print(" ########################################### ")
print("#                                           #")
print("#   BEM-VINDO AO SIMULADOR DE VISCOSIDADE!  #")
print("#                                           #")
print(" ########################################### ")
print("")

sample_counter = 1

while True:
	print("----------- Ensaio", sample_counter, "-----------\n")

	E = Experiment(
		window,
		canvas,
		(WIDTH, HEIGHT),
		scale, 
		2, # liquid width / cm
		5, # liquid height / cm
		(7850, 1400, 4.5) # ball density, fluid density, fluid viscosity (SI)
	)

	# User input (parameters)

	ok = False
	while not ok:
		print("Raio da esfera (0.5 a 2 mm): ", end="")
		radius = float(input())
		ok = (radius >= 0.5 and radius <= 2)

	print("Altura primeira marca (cm): ", end="")
	h1 = float(input())

	print("Altura segunda marca (cm): ", end="")
	h2 = float(input())


	E.AddMarker(h1)
	E.AddMarker(h2)

	E.AddBall(radius/10.)

	E.Run(0.0001, 20)


	# User input (continue?)
	ok = False
	while not ok:
		ans = input("\nNovo ensaio? (Sim/Nao)\n")
		ans = ans.lower()
		ok = ans in ["sim", "nao"]
	
	if ans == "nao":
		print("Bye Bye!")
		break
	
	canvas.delete("all")
	print("")
	sample_counter += 1
