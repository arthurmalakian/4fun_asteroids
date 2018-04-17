import turtle
from random import randint
class Screen():
    def __init__(self,width,height,title):
        self.height = height
        self.width = width
        self.title = title
        self.screen = turtle.Screen()
        self.screen.title(title)
        self.screen.setup(width,height,0,0)
        self.stars = True
    def clearScreen(self):
        pass
    def mainMenuSetup(self):
        self.screen.bgcolor("black")
        pen = turtle.Turtle()
        pen.penup()
        pen.setpos(((self.width/2)* -1) +10,((self.height/2) * -1) + 10)
        pen.pendown()
        pen.speed(0)
        pen.color("White")
        pen.hideturtle()
        for sides in range (4):
            if sides % 2 == 0:
                pen.fd(self.width-20)
                pen.lt(90)
            else:
                pen.fd(self.height-20)
                pen.lt(90)
        pen.penup()
        while self.stars == True:
            for x in range(self.width):
                for y in range(self.height):
                    pen.penup()
                    if randint(0,10000) == 1:
                        pen.setpos(x-300,y-200)
                        pen.dot(randint(2,4),self.starColors(randint(0,10)))
            self.stars = False
        logo = turtle.Turtle();
        logo.speed(0)
        logo.penup()
        logo.color("white")
        logo.setpos(0,100)
        logo.shape("turtle")
        pen.setpos(0,0)
        pen.write("Asteroids",False,"center",("Fixedsys", 26, "normal"))
        pen.setpos(0,-50)
        pen.write("Start",False,"center",("Fixedsys", 18, "normal"))
        pen.setpos(0, -100)
        pen.write("Scores",False,"center",("Fixedsys", 18, "normal"))
        pen.setpos(0, -150)
        pen.write("Quit",False,"center",("Fixedsys", 18, "normal"))
        turtle.done()
    def gameSetup(self):
        pass
    def starColors(self,num):
        switcher={
            0: "red",
            1: "blue",
            2: "green",
            3: "yellow",
        }
        return switcher.get(num,"white")