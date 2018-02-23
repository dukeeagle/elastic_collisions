#from visual import *
from vpython import *

from random import randint
L = 12
scene.range = L
T = 0.1

walls = []
balls = []

def create_ball(quantity):
    for i in range(0, quantity):
        ball_pos = randint(-5,5)
        ball_velocity = randint(-20,20)
        ball = sphere(pos=vector(ball_pos,0,0), radius=0.5, color=color.cyan)
        ball.velocity = vector(ball_velocity,randint(-15,15),randint(-15,15))
        print("Thy ball #" + str(ball) + "has been created in thy image")
        balls.append(ball)


def move_ball():
    for ball in balls:
        ball.pos = ball.pos + ball.velocity*deltat

wall_r = box(pos=vector((L/2)+(T/2),0,0), axis=vector(-1,0,0), length=T, height=L, width=L, color=color.red) #right wall
wall_l = box(pos=vector((-L/2)+(T/2),0,0), axis=vector(1,0,0), length=T, height=L, width=L, color=color.yellow) #left wall

wall_t = box(pos=vector(0,(L/2)+(T/2),0), axis=vector(0,-1,0), length=T, height=L+T, width=L+T, color=color.blue) #top wall
wall_b = box(pos=vector(0, (-L/2)+(T/2),0), axis=vector(0,1,0), length=T, height=L+T, width=L+T, color=color.green) #bottom wall

wall_back = box(pos=vector(0,0,(-L/2)+(T/2)), axis=vector(0,0,1), length=T, height=L+T, width=L+T, color=color.red) #back wall
wall_f = box(pos=vector(0,0,(L/2)+(T/2)), axis=vector(0,0,-1), length=T, height=L+T, width=L+T, color=color.yellow, visible=False) #front wall

#lamp = local_light(direction=(0,3,0), color=color.yellow)

walls = [wall_r, wall_l, wall_t, wall_b, wall_back, wall_f]
print(len(walls))

t=0
deltat=0.005

create_ball(2)

for wall in walls:
	#wall.color = color.blue
	wall.axisarrow = arrow(pos=wall.pos, axis=norm(wall.axis))
while t<6:
    rate(100)

    move_ball()
    t=t+deltat
