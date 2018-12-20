from tkinter import *
import time

root = Tk()
root.geometry('500x500')

c = Canvas(root, height = 500, width = 500)
i=1
j=1
x=3
y=3
#try:
while i<1000:
    
    l = c.create_line(i,j,x*x,y*y)
    i=x*x
    j=y*y
    x=(x+1)*(x+1)
    y=(y+1)*(y+1)
    c.pack()

c.mainloop()

#except KeyboardInterrupt:


