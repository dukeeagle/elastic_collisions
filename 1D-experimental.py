from visual import *
import time

balls = []

'''def create_ball(quantity):
    for range(0, quantity):
        ball_pos = random.randint(-6,6)
        ball_velocity = random.randin(-20,20)
        ball = sphere(pos=vector(ball_pos,0,0), radius=0.5, color=color.cyan)
        balls.append[ball]

def check_ball():
    for ball in balls: '''



ball_pos = random.randint(-6,6)
ball_velocity = random.randint(-20,20)
print x
ball = sphere(pos=vector(ball_pos,0,0), radius=0.5, color=color.blue)


ball2_pos = random.randint(-6,6)
ball2_velocity = random.randint(-20,20)
ball2 = sphere(pos=vector(ball2_pos,0,0), radius=0.5, color=color.blue)
ball2.velocity = vector(ball2_velocity,0,0)

triangle = shapes.triangle(pos=vector(0,0,0), length=5)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.blue)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.yellow)
wallT = box(pos=vector(0,6,0), size=vector(12,0.2,12), color=color.red)
wallBottom = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.green)
wallBack = box(pos=vector(0,0,-6), size=vector(12,12,0.2), color=color.green)
ball.velocity = vector(ball_velocity,0,0)
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
ball.trail = curve(color=ball.color)
deltat= 0.005
t = 0
scene.autoscale = False
while t<3:
    rate(100)

    #ball 1
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
        ball.color = color.cyan
    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
        ball.color = color.blue

    if ball.pos.y > wallT.pos.y:
        ball.velocity.y = -ball.velocity.y
        ball.color = color.cyan
    if ball.pos.y < wallBottom.pos.y:
        ball.velocity.y = -ball.velocity.y
        ball.color = color.blue

    if ball.pos.z < wallBack.pos.z:
        ball.velocity.z = -ball.velocity.z
    if ball.pos.z > 6:
        ball.velocity.z = -ball.velocity.z

    #ball2 2
    if ball2.pos.x > wallR.pos.x:
        ball2.velocity.x = -ball2.velocity.x
        ball2.color = color.cyan
    if ball2.pos.x < wallL.pos.x:
        ball2.velocity.x = -ball2.velocity.x
        ball2.color = color.blue

    if ball2.pos.y > wallT.pos.y:
        ball2.velocity.y = -ball2.velocity.y
        ball2.color = color.cyan
    if ball2.pos.y < wallBottom.pos.y:
        ball2.velocity.y = -ball2.velocity.y
        ball2.color = color.blue

    if ball2.pos.z < wallBack.pos.z:
        ball2.velocity.z = -ball2.velocity.z
    if ball2.pos.z > 6:
        ball2.velocity.z = -ball2.velocity.z


    if(abs(ball.pos.x - ball2.pos.x) < 2*ball.radius):
        cm_velocity = (ball.velocity.x + ball2.velocity.x) * 0.5

        ball_vcm = ball.velocity.x - cm_velocity
        ball2_vcm = ball2.velocity.x - cm_velocity

        ball_vcm = -ball_vcm
        ball2_vcm = -ball2_vcm

        ball.velocity.x = ball_vcm + cm_velocity
        ball2.velocity.x = ball2_vcm + cm_velocity

    #ball.color = color.blue
    ball2.pos = ball2.pos + ball2.velocity*deltat
    ball.pos = ball.pos + ball.velocity*deltat
    ball.trail.append(pos=ball.pos)
    varr.pos = ball.pos
    varr.axis = vscale*ball.velocity
    t= t + deltat
