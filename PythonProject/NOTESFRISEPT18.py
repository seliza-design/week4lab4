import numpy as np
from SimpleGraphics import *

MakeWindow(10, labels=False, bgcolor=PINK)

flag_width = 18
flag_height = 10
stripe_height = flag_height/13

for i in range(13):
    y = flag_height/2 - stripe_height/2 - i*stripe_height
    color = RED if i%2 == 0 else WHITE
    DrawRect(0,y,flag_width,stripe_height,FillColor=color, EdgeColor=color)
 #plot canton

    canton_width = 0.4*flag_width
    canton_height = stripe_height*7

    DrawRect(-flag_width/2 + canton_width/2, flag_height/2-canton_height/2,canton_width,canton_height,FillColor=BLUE,EdgeColor=BLUE)

    #plot stars
rows = 5
cols = 10
star_r = 0.25
x_start = -flag_width/2 + canton_width*0.05
y_start = flag_height/2 - canton_height*0.15 #tuning parameters attached to canton height
dx = canton_width/cols
dy= canton_height/rows

for i in range(rows):
    for j in range(cols):
        x = x_start+j*dx
        y = y_start-i*dy
        DrawStar(x,y,star_r,FillColor=WHITE,EdgeColor=WHITE)



ShowWindow()