'''
3/25/2021

Review

1. Import turtle library
import turtle # Top of the page

2. Create a pen / turtle
variable1 = turtle.Turtle()

3. (Optional) Create a screen / blank page
variable2 = turtle.Screen()

4. Movements

  a. forward
  variable1.fd(DISTANCE)
  variable1.forward(DISTANCE)

  b. backward
  variable1.backward(DISTANCE)
  variable1.bk(DISTANCE)

  c. turn right
  variable1.right(ANGLE)

  d. turn left
  variable1.left(ANGLE)

  e. pen up
  variable1.penup()

  f. pen down
  variable1.pendown()

  g. go home (0, 0; facing right)
  variable1.home()

  h. go to a specific point
  variable1.goto(X, Y)




1. Change turtle speed (0 ~ 10)
variable1.speed(SPEED)

2. Change width of line (0 ~ 10)
variable1.width(SIZE)

3. change color of pen
variable1.color(COLOR)

'''

# Draw a letter, Z


import turtle

pen = turtle.Turtle()
pen.speed(10)

colors = ["royal blue", "burlywood", "dark orange", "purple", "grey", "tan", "light coral"]

angle = 0
index = 0

while (angle < 360):

  pen.color(colors[index])
  index += 1
  if (index == 7):
    index = 0

  # Draw a square
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)

  angle += 10
  pen.home()
  pen.left(angle)