#Working on http://www.skulpt.org
 
import turtle


t = turtle.Turtle()
t.color(0)

def gallows(element):
  if element == 1:
    t.right(90)
    t.forward(120)
    t.backward(120)
  
  elif element == 2:
    t.left(90)
    t.forward(75)
  
  elif element == 3:
    t.backward(20)
    t.right(90)
    t.forward(20)
  
  elif element == 4:
    t.left(80)
    for i in range(30):
      t.forward(4)
      t.right(18)
    t.left(100)
  
  elif element == 5:
    t.forward(50)
    t.backward(40)
  
  elif element == 6:
    t.right(120)
    t.forward(30)
    t.backward(30)
  
  elif element == 7:
    t.left(240)
    t.forward(30)
    t.backward(30)
    t.right(120)
  
  elif element == 8:
    t.forward(40)
    t.left(45)
    t.forward(30)
    t.backward(30)
  
  elif element == 9:
    t.right(90)
    t.forward(30)
    t.backward(30)

def redraw_gallows(greshni_opiti):
    for element in range(greshni_opiti):
        gallows(element)


redraw_gallows(10)