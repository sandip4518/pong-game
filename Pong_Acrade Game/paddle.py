
from  turtle import *

class Paddle(Turtle):
	def __init__(self,x,y):
		super().__init__()
		self.x=x
		self.y=y
		self.shape("square")
		self.penup()
		self.color("white")
		self.shapesize(stretch_len=1, stretch_wid=5)
		self.goto(x, y)

	def up(self):
		new_y = self.ycor() + 20
		if new_y > 250:
			pass
		else:
			self.goto(x=self.xcor(), y=new_y)


	def down(self):
		new_y = self.ycor() - 20
		if new_y < -250:
			pass
		else:
			self.goto(x=self.xcor(), y=new_y)