import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape(name="circle")
    brad.color("white")
    brad.speed(5)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

def draw_circle_of_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape(name="circle")
    brad.color("yellow")
    brad.speed(5000)

    for i in range(1,36):
        brad.right(10)
        for j in range(0,4):
            brad.forward(100)
            brad.right(90)

    window.exitonclick()

def draw_rhombus(t):
    t.right(75)
    t.forward(50)
    t.right(30)
    t.forward(50)
    t.right(150)
    t.forward(50)
    t.right(30)
    t.forward(50)
    t.right(75)

def darw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()

    brad.shape(name="turtle")
    brad.color("blue")
    brad.speed(1000)
    for i in range(0,36*2):
        draw_rhombus(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(150)
    window.exitonclick()


# draw_square()
# draw_circle_of_square()
darw_flower()






