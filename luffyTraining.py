from tkinter import *
from random import *
from math import *
from time import *
from tkinter import*
import tkinter.font as tkFont
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()
#converts RGB code to hexcode
def rgb(r,g,b):
    return "#%s%s%s" % tuple([hex(c)[2:].rjust(2,"0") for c in (r,g,b)])
#empty arrays for background

skyColourRed = []#rgb vales for sky
skyColourBlue = []
skyColourGreen = []
house = []
roof = []
cloudx = []
cloudy = []
randx1 = 20
randx2 = 150
randy1 = 20
randy2 = 70

#background
#creates gradient effect for sky by implementing
for x in range (0,256):
    skyColourBlue.append(255)
    skyColourRed.append(150-round(x/2.2))
    skyColourGreen.append(round(x/5))
    screen.create_rectangle(0,x,800,x*3,outline = rgb(skyColourRed[x],skyColourGreen[x],skyColourBlue[x]), fill = rgb(skyColourRed[x],skyColourGreen[x],skyColourBlue[x]))

#clouds
for z in range(3): #loops through to create multiple layers of clouds
  for x in range(4):
    for n in range(25):
        cloudx.append(randint(randx1,randx2))
        cloudy.append(randint(randy1,randy2))
        z = 50
        screen.create_oval(cloudx[n], cloudy[n], cloudx[n]+z, cloudy[n]+z, fill="white", outline="white")
    cloudx.clear()
    cloudy.clear()
    spacex = randint(150,350)#spaces clouds each loop
    randx1 += spacex
    randx2 += spacex
  spacey = randint(70,120)#after creates 4 clouds, changes y value to add layer
  randy1 += spacey
  randy2 += spacey
  randx1 = randint(10,50)
  randx2 = randint(140,190)




screen.create_rectangle(0,430,800,500,fill = "dark green") #grass
#houses
for i in range(30):
    house.append(0)
    roof.append(0)
    x = randint(400,700)
    y = randint(435, 490)
    roofColour = choice(["LightSalmon2", "LightSalmon3", "LightSalmon4"])
    houseColour = choice(["burlywood1", "burlywood2", "burlywood3"])
    
    house[i] = screen.create_rectangle(x,y, x+25,y+15, fill=houseColour, outline = houseColour)
    roof[i] = screen.create_polygon(x-8,y+3, x+13,y-8, x+33,y+3, fill=roofColour)

#forest

for i in range(50):
    x = randint(0,390)
    y = randint(435,490)
    screen.create_rectangle(x,y,x+5,y+18, fill="saddle brown", outline = "saddle brown")

for i in range(300):
    x = randint(0,390)
    y = randint(415,490)
    size = randint(5,15)
    colour = choice(["dark green", "forest green"])
    screen.create_oval(x-size,y-size, x+size,y+size, fill=colour, outline=colour)

for i in range(10):
    x = randint(710,800)
    y = randint(435,490)
    screen.create_rectangle(x,y,x+5,y+18, fill="saddle brown", outline = "saddle brown")

for i in range(30):
    x = randint(710,800)
    y = randint(415,490)
    size = randint(5,15)
    colour = choice(["dark green", "forest green"])
    screen.create_oval(x-size,y-size, x+size,y+size, fill=colour, outline=colour)


screen.create_rectangle(0,500,800,600,fill = "brown" ) #floor
#Luffyy
screen.create_rectangle(100,500,110,430, fill = "#eab676")#legs
screen.create_rectangle(107,500,117,430, fill = "#eab676")
screen.create_polygon(97,440,120,440,120,470,97,470,fill = "blue")
screen.create_line(104,452,104,470)
screen.create_polygon(90,450,90,380,130,380,130,450,fill = "red",smooth = "true")#body
screen.create_oval(97,380,123,354,fill = "#eab676")#head
screen.create_arc(96,375,124,350,fill = "yellow",start = 0, extent = 180)
screen.create_line(96,362,124,362,width = 5, fill = "red")
screen.create_line(91,362.5,129,362.5,width = 3)
arm = screen.create_polygon(105,455,105,390,115,390,115,455,smooth = True, fill = "#eab676" )#arm

#Other guy
dummypole1 = screen.create_rectangle(300,500,315,350,fill = "brown")
dummypole2 = screen.create_rectangle(265,390,350,405,fill = "brown")
dummy1 = screen.create_polygon(275,450,340,450,330,375,285,375,smooth = True, fill = "#b6b79e")
dummy2 = screen.create_polygon(335,370,280,370,290,330,325,330,smooth = True, fill = "#b6b79e")

#text
text1=screen.create_text(200,300,font ="Elephant 30",text = "Gomu Gomu No!")
screen.update()
sleep(2)
screen.delete(text1)
text2 = screen.create_text(200,300,font ="Elephant 30",text = "JET GATLING GUN!")
screen.update()
sleep(2)
screen.delete(text2,arm,dummy1,dummy2)



y = [] #Arm values
x = [] 
arms = []
direction = []
arms2=[]
speed = []
x2 = [] #dummy starting position
dummySpeed = []
#starting values
for a in range(100):
    luffyArmPosition = randint(350,440)
    y.append(luffyArmPosition)
    x.append(100)
    arms.append(0)
    arms2.append(0)
    x2.append(300)
    speed.append(randint(50,80))
    dummySpeed.append(randint(5,10))
    



#initial arm position
for n in range(100):
  for b in range(100):
    a = randint(1,2)
    direction.append(a) #if values between 1 and 2 to determine going forwards or back
  for c in range(6):
    arms[c] = screen.create_polygon (x[c],y[c],x[c],y[c]+10,x[c]+150,y[c]+10,x[c]+150,y[c],fill = "#eab676",smooth = "true") #creates the different arms
    if n %2 == 1:
      if direction[c] == 1:#randomizes movement of arms and dummy (back and forth)
        x[c] -= speed[c]#movement
        x2[c] -= dummySpeed[c]
      else:
        x[c] += speed[c]
        x2[c] += dummySpeed[c]

    elif n%2 == 0: #resets to starting position
      x[c] = 100
      x2[c] = 300
 
  
  #remakes body for layering
  screen.create_polygon(90,450,90,380,130,380,130,450,fill = "red",smooth = "true")   
  #second layer of arms
  for d in range(7,12):
    arms2[d] = screen.create_polygon (x[d],y[d],x[d],y[d]+10,x[d]+150,y[d]+10,x[d]+150,y[d],fill = "#eab676",smooth = "true") #creates the different arms
    if n %2 == 1:
    #randomizes movement of arms (back and forth)
      if direction[c] == 1:
        x[d] -= randint(50,80)
      else:
        x[d] += randint(50,80)
    elif n%2 == 0: #resets to starting position
      x[d] = 100
  #dummy, in nested loop since only one copy is needed, don't want multiple makes everything more complicated
  dummy1 = screen.create_polygon(x2[a]-25,450,x2[a]+40,450,x2[a]+30,375,x2[a]-15,375,smooth = True, fill = "#b6b79e")
  dummy2 = screen.create_polygon(x2[a]+35,370,x2[a]-20,370,x2[a]-10,330,x2[a]+25,330,smooth = True, fill = "#b6b79e")
    



  screen.update()
  sleep(0.15)
  direction.clear() #clears array for true random each time
  for c in range(12): 
    screen.delete(arms[c],arms2[c]) #deletes
    screen.delete(dummy1,dummy2)
#recreates arm
arm = screen.create_polygon(105,455,105,390,115,390,115,455,smooth = True, fill = "#eab676" )
  

























screen.update()
screen.mainloop()
