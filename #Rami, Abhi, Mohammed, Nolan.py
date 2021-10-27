#Rami, Abhi, Mohammed, Nolan

'''
#Import turtle
import turtle as trtl
import time
t = trtl.Turtle()
wn = trtl.Screen()
#screen size set to be proportional to coordinates.
wn.setup(800, 800)
#Max speed
t.speed(0)
#pensize and turtle shape
t.pensize(3)
t.shape('circle')

wn.bgpic('800x800_coord.png')

def graph(tpe):
    #get slope (a) and verify input is whole number. While loop for try and exception.
    while True:
        wn.update()
        a = input('a = ')
        try:
            a = float(a)
        except ValueError:
            print('Whole numbers only please.')
            continue
        break

    #get y-intercept (b in linear, c in quadratic) and verify input is whole number. While loop for try and exception.
    while True:
        b = input('b = ')
        try:
            b = float(b)
        except ValueError:
            print('Whole numbers only please.')
            continue
        break

    #get c and verify input is whole number. While loop for try and exception.
    if tpe == 'quadratic':
        while True:
            c = input('c = ')
            try:
                c = float(c)
            except ValueError:
                print('Whole numbers only please.')
                continue
            break

    #calculations - can be  expanded for more function types
    mult = float(40)
    x_neg = float(-10)
    y_neg = float(a*x_neg + b)
    t.penup()
    t.goto(x_neg*mult, y_neg*mult)
    t.pendown()
    x = float(-10)

def arrows():
  t.penup()
  t.goto()

    if tpe == 'linear':
        while -10 <= x <= 10:
            y = a*x + b
            t.goto(x*mult, y*mult)
            x += 1
        while x=-9:
          value = 

    elif tpe == 'quadratic':
        while -10 <= x <= 10:
            y = a*(x**2) + b*x + c
            t.goto(x*mult, y*mult)
            x += 0.1
    else:
        print('Error, please try again.')
    


#execution
while True:
    tpe = input('Would you like to use linear or quadratic graphing calculator?: ')
    if tpe == 'linear':
        graph(tpe)
    elif tpe == 'quadratic':
        graph(tpe)
    else:
        print('Invalid option...')
        continue
    break




  
        
    

wn.mainloop()
'''
import turtle as trtl
t = trtl.Turtle()


l = 50
t.goto(-(0.5*float(l))
for i in range(3):
  t.fd(l)
  t.right(120)

wn = trtl.Screen()
wn.mainloop()

