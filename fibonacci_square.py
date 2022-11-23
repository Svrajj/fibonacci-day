import turtle
import math


wn = turtle.Screen()
wn.setup(1000,800)
myTurtle = turtle.Turtle()  
myTurtle.pensize(3)


def main():             
    valueOne = 0
    valueTwo = 1
    fib = 1
    for i in range(8):                      
        myTurtle.right(90)                  
        drawSq(fib*20)                      
        fib = valueOne + valueTwo           
        valueOne = valueTwo
        valueTwo = fib
        
def drawSq(sides):
    for n in range(6):                    
        myTurtle.forward(sides)            
        myTurtle.left(90)                  


def sprial():
    r = 20                                 
    angle = 90
    myTurtle.right(90)                     
    myTurtle.penup()
    myTurtle.setpos(0,0)                  
    myTurtle.pendown()
    arc(20, angle)                         
    arc(20, angle)                         
    arc(40, angle)                         
    arc(60, angle)                         
    arc(100, angle)                       
    arc(160,angle)                         
    arc(260,angle)                        
    arc(420,angle)                        


def arcLine(n, length, angle):            
    for i in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)


def arc(r, angle):                        
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
   
    myTurtle.left(step_angle/2)
    arcLine(n, step_length, step_angle)
    myTurtle.right(step_angle/2)


main()                                     
sprial()                                   
wn.exitonclick()     
myTurtle.done()