from tkinter import *
import time

canvas_width = 500
canvas_height = 500


def paint(master):
    i=1
    j=1
    x=3
    y=3
    while i<100:
        python_green = "#476042"
        x1, y1 = master.i, master.j
        x2, y2 = master.x, master.y
        w.create_oval(x1, y1, x2, y2, fill=python_green)
        i=x*x
        j=y*y
        x=(x+1)*(x+1)
        y=(y+1)*(y+1)
        time.sleep(0.1)
        print (x)
        print (y)
        print (i)
        print (j)



c = Tk()
c.title("Points")
w = Canvas(c,
           width=canvas_width,
           height=canvas_height)
w.bind(paint)
w.mainloop()