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
    def __init__(self, color, x, y, xspeed, yspeed):
        self.color = color
        self.shape = canvas.create_oval(10, 10, x, y, fill=color)
        self.trail_line = canvas.create_line(10, 10, 10, 10)
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.pos = canvas.coords(self.shape)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        self.pos = canvas.coords(self.shape)
        canvas.coords(self.trail_line)[2] = self.pos[2]
        canvas.coords(self.trail_line)[3] = self.pos[3]
        if self.pos[3] > 800 or self.pos[1] < 0:
            self.yspeed *= -1
            #self.yspeed = self.yspeed-1 if self.yspeed < 0 else self.yspeed+1
            canvas.configure(bg="blue")
            return TRUE
        if self.pos[2] > 1000 or self.pos[0] < 0:
            self.xspeed *= -1
            #self.xspeed = self.yspeed - 1 if self.yspeed < 0 else self.xspeed + 1
            canvas.configure(bg="yellow")
            return True
        return False


balls = [Ball("orange", 10, 10, 2, 4)]

while TRUE:
    for ball in balls:
        if(ball.move()) :
            balls.append(Ball("orange", ball.pos[0], ball.pos[1], random.randrange(1, 5), random.randrange(1, 5)))
    canvas.pack()
    tk.update()
    time.sleep(0.01)
