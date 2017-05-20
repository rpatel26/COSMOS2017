'''
File Name: square.py

Discription: this module will draw two squares where one of the square is 
              incsribed inside the other square.

Task: Go through the code line by line and spot the error. Think about how the
      code can be fixed to make one square inscribed in the other.
'''

from turtle import Turtle,Screen

donatello = Turtle()
world = Screen()
donatello.speed(1)

donatello.forward(200)
donatello.right(90)
donatello.forward(200)
donatello.right(90)
donatello.forward(200)
donatello.right(90)
donatello.forward(200)

donatello.right(90)
donatello.forward(50)
donatello.right(90)
donatello.forward(50)
donatello.pendown()

donatello.left(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(125)
donatello.right(90)
donatello.forward(100)



world.exitonclick()
