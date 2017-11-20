import random
import sys
import os
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=1000, height=800, bg = "white")
tk.title = "Graphics"
canvas.pack()

class Ball:
    def __init__(self, color, position, xspeed, yspeed):
        self.color = color
        self.shape = canvas.create_oval(position, fill=color)
        #self.trail_line = canvas.create_line(10, 10, 10, 10)
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.pos = position

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        self.pos = canvas.coords(self.shape)
        #canvas.coords(self.trail_line)[2] = self.pos[2]
        #canvas.coords(self.trail_line)[3] = self.pos[3]
        if self.pos[3] > 800 or self.pos[1] < 0:
            self.yspeed *= -1
            balls.append(Ball("orange", ball.pos, random.randint(5, 8), random.randint(5, 8) * (self.yspeed/abs(self.yspeed))))
            #self.yspeed = self.yspeed-1 if self.yspeed < 0 else self.yspeed+1
            canvas.configure(bg="blue")
            return True
        if self.pos[2] > 1000 or self.pos[0] < 0:
            self.xspeed *= -1
            balls.append(Ball("orange", ball.pos, random.randint(5, 8) * self.xspeed/abs(self.xspeed), random.randint(5, 8)))
            #self.xspeed = self.yspeed - 1 if self.yspeed < 0 else self.xspeed + 1
            canvas.configure(bg="yellow")
            return True
        return False


balls = [Ball("orange", [10, 10, 60, 60], 2, 4)]

while TRUE:
    for ball in balls:
        if ball.move() :
            canvas.move(balls[len(balls) - 1].shape, balls[len(balls) - 1].xspeed, balls[len(balls) - 1].yspeed)
    canvas.pack()
    tk.update()
    time.sleep(0.01)
