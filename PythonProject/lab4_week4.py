import random

from packaging.tags import platform_tags

import matplotlib.pyplot as plt
import numpy as np


from time import sleep as pause

from SimpleGraphics import *

# Part 1 warm up

MakeWindow(10, labels=False, bgcolor=WHITE)
Title("Shapes Part 1", FontColor=BLACK, FontSize=16)
DrawRect(0,6,3,4, FillColor=RED,EdgeColor=BLACK, EdgeWidth=1)
DrawText(0,9,"rectangle",FontColor=BLACK, FontSize=16)
DrawDisk(0,-7,2,FillColor=PINK, EdgeWidth=1)
DrawText(2,-7,"circle",FontColor=BLACK,FontSize=16)
DrawStar(-8,-1,2,theta=0.0, FillColor=BLUE, EdgeWidth=1)
DrawText(-6,-1,"star",FontColor=BLACK,FontSize=16)
DrawLineSeg(3,3,7,7, LineColor=BLACK, LineWidth=5)
DrawText(4,3,"Line",FontColor=BLACK,FontSize=16)
DrawPoly([0, 3.8, 2.35, -2.35, -3.8], [-4, -1.24, 3.24, 3.24, -1.24], FillColor=GREEN, EdgeColor=BLACK, EdgeWidth=1)
DrawText(0,0,"pentagon",FontColor=BLACK,FontSize=16)
ShowWindow()

#Part 2

def starrynight():
    M = 12
    MakeWindow(M , labels=True, bgcolor=DARKBLUE)
    Title("Starry Night")

    num_stars= 55
    for _ in range(num_stars):
        x= random.uniform(-M +1, M - 1)
        y= random.uniform(-M + 1, M - 1)
        r= random.uniform(0.1,0.4)
        twinkle = random.random() < .2

        if twinkle:
            color = [1.0,1.0,random.uniform(0.7,1.0)]
            angle = random.uniform(0, 360)

        else:
            color= WHITE
            angle = 0

        DrawStar(x,y,r, theta=angle, FillColor=color, EdgeWidth=0)
    DrawDisk(5,5,3,FillColor=[1.0,1.0,0.66], EdgeColor= WHITE,EdgeWidth=0)
    ShowWindow()
if __name__ == "__main__":
    starrynight()


#Part 3: Creative : I chose a campsite scene because it reused a lot of shapes that I was already familiar with along with newer ideas like creating different colors (added it to the SimpleGraphics module

import random

def campsite():
    M = 12
    MakeWindow(M, labels=True, bgcolor=DARKBLUE)
    Title("Night time Campsite")

    for _ in range(30):
        x = random.uniform(-11, 11)
        y = random.uniform(2, 11)

        DrawStar(x, y, 0.25,theta=0,FillColor=WHITE,EdgeWidth=0)

    DrawDisk(7, 7, 2.5, FillColor=YELLOW, EdgeColor=YELLOW, EdgeWidth=0)
    # Ground
    DrawPoly([-12, 12, 12, -12],[-12, -12, -6, -6],FillColor=GREEN,EdgeColor=GREEN)

    # Tent
    DrawPoly([-6, 0, 6],[-6, 1, -6],FillColor=BLUE,EdgeColor=BLACK)

    # Tent entrance
    DrawPoly([-1.5, 0, 1.5],[-6, -2.5, -6],FillColor=BLACK, EdgeColor=BLACK)

    # Campfire logs
    DrawPoly([3, 7, 7.5, 3.5], [-10, -8.5, -9.2, -10.7], FillColor=BROWN, EdgeColor=BLACK)

    DrawPoly([3.5, 7.5, 7, 3],[-8.8, -10.2, -10.8, -9.5], FillColor=BROWN, EdgeColor=BLACK)

    # Fire
    DrawPoly([5.5, 4, 5, 5.5, 7, 7], [-8.5, -6, -7, -4.5, -7, -6],FillColor=RED, EdgeColor=YELLOW)

    # Tree trunk
    DrawPoly([-10, -8, -8, -10], [-6, -6, 3, 3], FillColor=BROWN, EdgeColor=BLACK)

    # Tree
    DrawPoly([-12, -9, -6, -12], [1, 6, 1, 1], FillColor=GREEN, EdgeColor=GREEN)

    # Shooting star
    DrawPoly([-7, -3, -3.2, -7.5],[8, 5, 5.3, 8.3],FillColor=WHITE,EdgeColor=WHITE)

    # Shooting star tip
    DrawStar(-3, 5, 0.5,theta=0,FillColor=YELLOW,EdgeWidth=0)

    ShowWindow()


if __name__ == "__main__":
    campsite()



