import random
import sys
import os
import time
from tkinter import *
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findMidpoint(p1, p2):
    return Point((p1.x + p2.x)/2, (p1.y + p2.y)/2)


def createTriangle(p1, p2, p3) :
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, width = 1)
    canvas.create_line(p2.x, p2.y, p3.x, p3.y, width = 1)
    canvas.create_line(p3.x, p3.y, p1.x, p1.y, width = 1)


def createSierpinski(x, y, L, n) :
    if n > 0 :
        time.sleep(.005)
        createTriangle(Point(x,y), Point(x + L, y), Point(x + L/2, y + (L/2) * math.sqrt(3)))
        tk.update()
        createSierpinski(x-L/4, y + (L/2) * math.sqrt(3)/2, L/2, n-1)
        createSierpinski(x + L/4, y - (L/2) * math.sqrt(3)/2, L/2, n-1)
        createSierpinski(x + (L - L/4), y + (L/2) * math.sqrt(3)/2, L/2, n-1)

size = 1000
tk = Tk()
canvas = Canvas(tk, width=size, height=size, bg = "white")
tk.title = "Triangles"
tk.resizable (False, False)
tk.update()
canvas.pack()

degrees = 8
x = size/4.0
y = size/2.0
L = (size * 3.0)/8.0

createSierpinski(x, y, L, degrees)

canvas.mainloop()

