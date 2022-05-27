from tkinter import *
import time
from math import pi

class Fluid:
	def __init__(self, canvas, size, w, h):
		self.image = canvas.create_rectangle(
			(size[0] - w)/2, size[1] - h, 
			(size[0] + w)/2, size[1], 
			fill="cyan"
		)
		self.widht = w
		self.height = h


class Experiment:
	def __init__(self, window, canvas, size, scale, parameters):
		self.window = window
		self.canvas = canvas
		self.size = size
		self.scale = scale
		self.fluid = Fluid(canvas, size, 10*scale, 25*scale) # fluid 10 cm x 25 cm

		# scale legend
		canvas.create_line(size[0]/10, size[1]/10, size[0]/10, size[1]/10 +2* scale, arrow = BOTH)
		canvas.create_text(size[0]/10, size[1]/10 + scale, text=" 2 cm", anchor = W)

		self.ball_density = parameters[0]
		self.fluid_density = parameters[1]
		self.viscosity = parameters[2]
		
	def AddMarker(self,h):
		self.canvas.create_line(
			  self.size[0]/10, self.size[1] - h*self.scale, 
			9*self.size[0]/10, self.size[1] - h*self.scale
		)

	def AddBall(self, radius):
		w = self.size[0]
		h = self.size[1]
		
		self.ball = self.canvas.create_oval(
			w/2 - radius*self.scale, h - self.fluid.height - radius * self.scale,
			w/2 + radius*self.scale, h - self.fluid.height + radius * self.scale,
			fill = "yellow"
		)
		self.radius = radius
		self.mass = 4*pi/3*(radius/100)**3 * self.ball_density
		self.velocity = 0

	def Run(self, dt):
		#time.sleep(2)
		while True:
			self.canvas.move(self.ball, 0, self.velocity)
			dv = dt* 9.81*(1- self.fluid_density/self.ball_density) * self.scale 
			dv -= dt* 6*pi*self.viscosity* self.radius/100. * (self.velocity/self.scale) /self.mass * self.scale 
			
			self.velocity += dv

			self.window.update()
			time.sleep(dt)
			if self.canvas.coords(self.ball)[3] >= self.size[1]:
				break
