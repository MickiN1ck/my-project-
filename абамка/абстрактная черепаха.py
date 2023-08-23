import turtle

from random import randint

turtle.shape('turtle')

for i in range(10):
    turtle.goto(randint(-200,200), randint(-200,200))
    a = randint(10, 100)
    for r in range(4):
        turtle.forward(a)
        turtle.right(90)

turtle.mainloop()