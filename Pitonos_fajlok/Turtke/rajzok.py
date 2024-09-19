import turtle

def sziv(pen):
    pen.reset()
    pen.speed("fastest")
    pen = turtle.Turtle()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    for i in range(200):
        pen.right(1)
        pen.forward(1)
    pen.left(120)
    for i in range(200):
        pen.right(1)
        pen.forward(1)
    pen.forward(112)
    pen.end_fill()


def kocka(pen):
    pen.reset()
    pen.speed("fastest") 
    pen.color("orange")           
    for i in range(4): 
        pen.forward(100) 
        pen.left(90) 
    pen.goto(50,50) 
    for i in range(4): 
        pen.forward(100) 
        pen.left(90) 
    pen.goto(150,50) 
    pen.goto(100,0) 
    pen.goto(100,100) 
    pen.goto(150,150) 
    pen.goto(50,150) 
    pen.goto(0,100)

def kor(pen):
    pen.reset()
    pen.speed("fastest")
    pen.color("green")
    for i in range(360):
        pen.forward(1)
        pen.left(1)

def crazy(pen):
    pass

def hatszog(pen):
    pen.reset()
    pen.speed("fastest")
    pen.color("yellow")
    for i in range(6):
        pen.forward(90)
        pen.left(60)