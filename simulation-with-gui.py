#! python2
from visual import *
import visual as vs
#from vpython import *
import wx
from random import randint
L = 12
scene.range = L
T = 0.1

colors = [color.red, color.green, color.blue, color.yellow, color.cyan, color.magenta]

walls = []
balls = []

run = True
win = vs.window(width=1024, height=720, menus=False, title='ELASTIC COLLISIONS BBY')
scene = vs.display( window=win, width=830, height=690, forward=-vs.vector(1,1,2))

total_balls = 0

x1 = scene.width + 5
pan = win.panel
pan.SetSize((1024,720))

#temp_ball = sphere(pos=vector(0,0,0), radius=0.5, color=color.green)

wx.StaticText( pan, pos=(x1,10),
label = "Welcome to Luke's Zone.\n Select your desired \nparameters and \nget in there!" )


wx.StaticText( pan, pos=(x1,105),
label = "# of Balls:" )
value = wx.TextCtrl( pan, pos=(x1, 125))

#Setting average kinetic energy / temperature
wx.StaticText( pan, pos=(x1, 170),
label = "Size of Cube:")
slider = wx.Slider( pan, pos=(x1, 195))
slider.SetValue(12)
slider.SetMax(24)
slider.SetMin(0.1)


def change_walls(evt):
    global walls
    global L
    L = slider.GetValue()
    #print(slider.GetValue())
    walls = [] #clear out the previous list of walls

    wall_r = box(pos=vector((L/2)+(T/2),0,0), axis=vector(-1,0,0), length=T, height=L, width=L, color=color.red) #right wall
    wall_l = box(pos=vector((-L/2)+(T/2),0,0), axis=vector(1,0,0), length=T, height=L, width=L, color=color.yellow) #left wall

    wall_t = box(pos=vector(0,(L/2)+(T/2),0), axis=vector(0,-1,0), length=T, height=L+T, width=L+T, color=color.blue) #top wall
    wall_b = box(pos=vector(0, (-L/2)+(T/2),0), axis=vector(0,1,0), length=T, height=L+T, width=L+T, color=color.green) #bottom wall

    wall_back = box(pos=vector(0,0,(-L/2)+(T/2)), axis=vector(0,0,1), length=T, height=L+T, width=L+T, color=color.red) #back wall
    wall_f = box(pos=vector(0,0,(L/2)+(T/2)), axis=vector(0,0,-1), length=T, height=L+T, width=L+T, color=color.yellow, visible=False) #front wall

    walls = [wall_r, wall_l, wall_t, wall_b, wall_back, wall_f]


slider.Bind(wx.EVT_SCROLL, change_walls)

def clear_balls():
    global slider
    print(slider.GetValue())
    #global temp_ball
    for ball in balls:
        #ball.visible = False
        #ball.delete
        ball.pos = vector(100,100,100)
        #del ball
        #del temp_ball
        #print(ball)


def hHelp(evt): # re "HELP" button
    wx.MessageBox(
"""This program is pretty simple at the moment. What else is there to understand?
""", 'HELP',  wx.OK  )

def configure_new_instance(evt):
    global scene
    global value
    new_balls = int(value.GetValue())
    print("Gotcha!")
    print(new_balls)

    scene.delete()

    scene = vs.display( window=win, width=830, height=690, forward=-vs.vector(1,1,2))

    #clear_balls()
    #new_win = vs.window(width=1024, height=720, menus=False, title='ELASTIC COLLISIONS BBY v2')
    create_ball(new_balls)
    change_walls(0)

def Button1( label, y, func):
   bb = wx.Button( pan, label=label, pos=(x1+5,y), size = (150,40))
   bb.Bind(wx.EVT_BUTTON, func)

Button1('HELP',          500, hHelp )


def create_ball(quantity):

    for i in range(0, quantity):
        ball_pos = randint(-5,5)
        ball_velocity = randint(-15,15)
        ball_velocity_y = randint(-15,15)
        ball_velocity_z = randint(-15,15)
        ball_radius = random.uniform(0.5,1.2)

        ball = sphere(pos=vector(ball_pos,0,0), radius=ball_radius, color=colors[randint(0,5)])
        ball.mass = ball_radius * 1.2
        #ball.velocity = vector(ball_velocity,randint(-15,15),randint(-15,15))
        ball.velocity=vector(ball_velocity,ball_velocity_y,ball_velocity_z)
        print("Thy ball #" + str(ball) + "has been created in thy image")
        balls.append(ball)

Button1('Update',          550, configure_new_instance)


def move_ball():
    global t
    global deltat
    for ball in balls:
        ball.pos = ball.pos + ball.velocity*deltat
        for other_ball in balls: #ball collisions
            #ball_one_overlap = ball.radius + 0.5*T
            if (not(other_ball == ball)): #prevent calculuating collision between ball and itself
        	   #print("it's a dupe!")
                ball.norm=norm(ball.axis)

                ball_dist = ball.pos - other_ball.pos
                #direction = norm(ball_dist)
                #ball_dist_vector = dot(ball_dist, direction)
                #if(abs(ball.pos.x - other_ball.pos.x) < (ball.radius + other_ball.radius)): #check collision
                if(mag(ball_dist) < (ball.radius + other_ball.radius)): #check collision
                    direction=norm(ball_dist)

                    overlap = (ball.radius + other_ball.radius) - dot(ball_dist, direction)
                    #btime = (((2*ball.radius - abs(ball.pos.x - other_ball.pos.x))/(abs(ball.velocity.x - other_ball.velocity.x))))
                    #btime = (((2*ball.radius - mag(ball.pos - other_ball.pos))/(mag(ball.velocity - other_ball.velocity))))
                    vn = dot(ball.velocity - other_ball.velocity, direction)
                    btime = -overlap/vn

                    ball.pos = ball.pos - btime*ball.velocity
                    other_ball.pos = other_ball.pos - btime*other_ball.velocity

                    cm_velocity = (ball.mass*ball.velocity + other_ball.mass*other_ball.velocity) / (ball.mass + other_ball.mass)

                    ball_vcm = ball.velocity - cm_velocity
                    other_ball_vcm = other_ball.velocity - cm_velocity

                    ball_vcm = ball_vcm - 2*dot(ball_vcm, direction)*direction
                    other_ball_vcm = other_ball_vcm - 2*dot(other_ball_vcm, direction)*direction


                    ball.velocity = ball_vcm + cm_velocity
                    other_ball.velocity = other_ball_vcm + cm_velocity

                    ball.pos = ball.pos + ball.velocity*btime
                    other_ball.pos = other_ball.pos + other_ball.velocity*btime

        for wall in walls: #wall collisions
        	wall.norm=norm(wall.axis)
        	dist=dot(ball.pos-wall.pos, wall.norm)
        	if(dist < (ball.radius + T/2)):
        		overlap = (ball.radius + T/2) - dist #overlap between ball and wall
        		vn = dot(ball.velocity, wall.norm) #velocity of normal vector
        		time = -overlap/vn
        		ball.pos = ball.pos - ball.velocity*time
        		ball.velocity = ball.velocity - 2*vn*wall.norm
        		ball.pos = ball.pos + ball.velocity*time

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
deltat=0.01


'''for wall in walls:
	#wall.color = color.blue
	wall.axisarrow = arrow(pos=wall.pos, axis=norm(wall.axis))'''
def run():
    global t
    global deltat

    while t<100:
        rate(100)

        move_ball()
        t=t+deltat


def main():
    #print("Greetings!")
    #spheres_to_make = int(raw_input("How many spheres would you like?"))
    #avg_radius = raw_input("Average radius?")
    #avg_temperature = raw_input("Average temperature?")
    create_ball(2)
    run()

if __name__ == "__main__":
    main()
