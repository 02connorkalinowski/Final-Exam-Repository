#Simple pong game
#3.12.19
# Connor

import turtle

wn = turtle.Screen()
wn.title("Pong by Connork.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Main-game-loop
while True:
	wn.update()
# Paddle-A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)



# Paddle B



# Ball