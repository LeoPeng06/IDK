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

armSpeed = []#Arm move speed
block = [] #block luffy hits
text = [] #Text box

#background
#creates gradient effect for sky by implementing
for x in range (0,256):
    skyColourBlue.append(255)
    skyColourRed.append(150-round(x/2.2))
    skyColourGreen.append(round(x/5))
    screen.create_rectangle(0,x,800,x*3,outline = rgb(skyColourRed[x],skyColourGreen[x],skyColourBlue[x]), fill = rgb(skyColourRed[x],skyColourGreen[x],skyColourBlue[x]))

screen.create_rectangle(0,500,800,600,fill = "brown" ) #floor


y = [] #Arm position
x = [] 
arms = []
#starting values
for a in range(100):
    luffyArmPosition = randint(380,460 )
    y.append(luffyArmPosition)
    x.append(100)
    arms.append(0)
#arm speed
for b in range(100):
    a = randint(1,2)
    armSpeed.append(a) #if values between 1 and 2 to determine going forwards or back
print(len(y))
print(len(x))

#initial arm position
for n in range(100):
  for c in range(15):
    arms[c] = screen.create_polygon(x[c],y[c],x[c],y[c]+10,x[c]+100,y[c]+10,x[c]+100,y[c],fill = "black",smooth = "true") #creates the different arms

    #randomizes movement of arms (back and forth)
    if armSpeed[n] == 1:
      x[c] -= 50
    else:
      x[c] += 50
    
  screen.update()
  sleep(0.1)
  for c in range(15):
    screen.delete(arms[c])
  

























screen.update()
screen.mainloop()