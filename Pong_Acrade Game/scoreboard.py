from  turtle import  Turtle




class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.l_score = 0
		self.r_score = 0
		self.color("white")
		self.hideturtle()
		self.penup()
		self.update()
	def update(self):
		self.clear()
		self.goto(-100, 200)
		self.write(f"{self.l_score}", align="center", font=("Courier", 60, "bold"))
		self.goto(100, 200)
		self.write(f"{self.r_score}", align="center", font=("Courier", 60, "bold"))

	def l_point(self):
		self.l_score+=1
		self.update()

	def r_point(self):
		self.r_score+=1
		self.update()



