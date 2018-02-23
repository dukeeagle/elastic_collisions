from visual import *
#from vpython import *

from random import randint
L = 12
scene.range = L
T = 0.1

walls = []
balls = []

def create_ball(quantity):
    for i in range(0, quantity):
        ball_pos = randint(-6,6)
        ball_velocity = randint(-20,20)
        ball_velocity_y = randint(-20,20)
        ball_velocity_z = randint(-20,20)
        ball = sphere(pos=vector(ball_pos,0,0), radius=0.5, color=color.cyan)
        print("Thy ball #" + str(ball) + "has been created in thy image")
        balls.append(ball)

wall_r = box(pos=vector((L/2)+(T/2),0,0), axis=vector(-1,0,0), length=T, height=L, width=L, color=color.red) #right wall
wall_l = box(pos=vector((-L/2)+(T/2),0,0), axis=vector(1,0,0), length=T, height=L, width=L, color=color.yellow) #left wall

wall_t = box(pos=vector(0,(L/2)+(T/2),0), axis=vector(0,-1,0), length=T, height=L+T, width=L+T, color=color.blue) #top wall
wall_b = box(pos=vector(0, (-L/2)+(T/2),0), axis=vector(0,1,0), length=T, height=L+T, width=L+T, color=color.green) #bottom wall

wall_back = box(pos=vector(0,0,(-L/2)+(T/2)), axis=vector(0,0,1), length=T, height=L+T, width=L+T, color=color.red) #back wall
wall_f = box(pos=vector(0,0,(L/2)+(T/2)), axis=vector(0,0,-1), length=T, height=L+T, width=L+T, color=color.yellow, visible=False) #front wall

#lamp = local_light(direction=(0,3,0), color=color.yellow)

walls = [wall_r, wall_l, wall_t, wall_b, wall_back, wall_f]
print(len(walls))


for wall in walls:
	rate(1)
	#wall.color = color.blue
	wall.axisarrow = arrow(pos=wall.pos, axis=norm(wall.axis))

create_ball(6)
