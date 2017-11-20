import random
import sys
import os
import time
from Tkinter import *
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findMidpoint(p1, p2):
    return Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)


def doSierpinski(x, y, L, n) :
    if n > 0 :
        time.sleep(.005)
        canvas.create_polygon(x,y, x + L, y, x + L/2, y + (L/2) * math.sqrt(3), fill = "red" if n == 6 else "orange" if n==5 else "yellow" if n==4 else "green" if n==3 else "blue" if n==2 else "purple" if n==1 else "black")
        tk.update()
        doSierpinski(x - L / 4, y + (L / 2) * math.sqrt(3) / 2, L / 2, n - 1)
        doSierpinski(x + L / 4, y - (L / 2) * math.sqrt(3) / 2, L / 2, n - 1)
        doSierpinski(x + (L - L / 4), y + (L / 2) * math.sqrt(3) / 2, L / 2, n - 1)

size = 1000
tk = Tk()
canvas = Canvas(tk, width=size, height=size, bg = "white")
tk.title = "Triangles"
tk.resizable (False, False)
tk.update()
canvas.pack()

degrees = 6

x = size/4.0
y = size/2.0
L = (size * 3.0)/8.0

doSierpinski(x, y, L, degrees)

canvas.mainloop()

