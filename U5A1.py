from tkinter import *
from random import *
from math import *
from time import *
from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()
#converts RGB code to hexcode
def rgb(r,g,b):
    return "#%s%s%s" % tuple([hex(c)[2:].rjust(2,"0") for c in (r,g,b)])
#empty arrays
petals = []  #Background related
petalSpeed = []
skyColourRed = []#rgb vales for sky
skyColourBlue = []
skyColourGreen = []
luffyArm = [] #position of arm
block = [] #block luffy hits
text = [] #Text box

#background
#creates gradient effect for sky
for x in range (0,256):
    skyColourBlue.append(255)
    skyColourRed.append(150-round(x/2.2))
    skyColourGreen.append(round(x/5))
    screen.create_rectangle(0,x,800,x*3,outline = rgb(skyColourRed[x],skyColourGreen[x],skyColourBlue[x]), fill = rgb(r,g,b))
screen.create_rectangle(0,500,800,600,fill = "brown" ) #floor
#Luffy character

#legs
screen.create_rectangle(20,490,30,440, fill = "black")
screen.create_rectangle(40,490,50,440, fill = "black")

#body
screen.create_polygon(15,440,15,380,55,380,55,440,fill = "red",smooth = "true")
#head
screen.create_oval(22,380,48,354,fill = "orange")

#back arm
screen.update()
screen.mainloop()