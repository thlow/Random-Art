tom = Turtle()
tom.shape('turtle')
tom.width(5)
tom.tracer(100)

for count in range(50):
    tom.left(360/50)
    for count in[1,2,3]:
        tom.color('gold')
        tom.left(90)
        tom.forward(100)
        tom.right(90)
        tom.forward(50)
        tom.left(90)
        tom.forward(100)
        tom.right(90)
        tom.color('orange')
        tom.forward(50)
        tom.right(90)
        tom.color('yellow')
        tom.forward(50)
        tom.left(90)
        tom.forward(100)
        tom.right(90)
        tom.forward(100)
        tom.left(90)
        tom.penup()
        tom.forward(20)
        tom.pendown()
        
        tom.left(90)
