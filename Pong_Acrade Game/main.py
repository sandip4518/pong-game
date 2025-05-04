from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.tracer(0)
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong game")

r_paddle = Paddle(x=370,y=0)
l_paddle = Paddle(x=-370,y=0)
screen.listen()




screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)
screen.onkey(key="W",fun=l_paddle.up)
screen.onkey(key="S",fun=l_paddle.down)

ball = Ball()
scoreboard = Scoreboard()

game_is_on=True



while game_is_on:

	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	#detect collision with wall
	if ball.ycor() > 270 or ball.ycor() < -270:
		ball.bounce_y()

	#detect collision with the paddle
	if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
		ball.bounce_x()
	#detect ball misses the l_paddle
	if ball.xcor() < -410:
		scoreboard.r_point()
		time.sleep(0.5)
		ball.reset_position()

	if ball.xcor() > 410:
		scoreboard.l_point()
		time.sleep(0.5)
		ball.reset_position()























screen.exitonclick()