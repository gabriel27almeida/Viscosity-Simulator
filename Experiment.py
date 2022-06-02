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
	def __init__(self, window, canvas, size, scale, fluid_width, fluid_height,parameters):
		self.window = window
		self.canvas = canvas
		self.size = size
		self.scale = scale
		self.fluid = Fluid(canvas, size, fluid_width*scale, fluid_height*scale)

		# scale legend
		canvas.create_line(size[0]/10, size[1]/10, size[0]/10, size[1]/10 + scale, arrow = BOTH)
		canvas.create_text(size[0]/10, size[1]/10 + scale/2, text=" 1 cm", anchor = W)

		self.ball_density = parameters[0]
		self.fluid_density = parameters[1]
		self.viscosity = parameters[2]
		
	def AddMarker(self,h):
		# Horizontal marker
		self.canvas.create_line(
			  self.size[0]/10, self.size[1] - h*self.scale, 
			9*self.size[0]/10, self.size[1] - h*self.scale
		)

	def AddBall(self, radius):
		# canvas size
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
		self.distance = 0 # to store distance travelled in each frame

	def Run(self, dt, FPS):
		steps_per_frame = int(1./FPS/dt)

		i = 0
		start_time = time.time()
		while True:
			# Euler solver
			a = 9.81*(1 - self.fluid_density/self.ball_density)
			a -= 6*pi*self.viscosity* self.radius/100. * self.velocity /self.mass
			
			dv = a * dt
			
			self.velocity += dv
			self.distance += self.velocity * dt

			# Make new frame
			if (i % (steps_per_frame) == 0):
				# Sleep if early
				time.sleep(max(start_time + (i+1) * dt - time.time(), 0))
				self.canvas.move(self.ball, 0, self.distance * 100 * self.scale)
				self.window.update()
				self.distance = 0

			# if bottom reached
			if self.canvas.coords(self.ball)[3] >= self.size[1]:
				break

			i += 1
