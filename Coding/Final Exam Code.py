#Simple pong game
#3.12.19
# Connor
'''
This is my simple Pong game that will be a multiplayer game with a workign score and sound effects.
Credit: @TokyoEdTech
'''

import turtle

wn = turtle.Screen()
wn.title("Pong by Connork.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Main-game-loop
# Paddle-A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)





# Paddle-b

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0)


while True:
	wn.update()



# Ball