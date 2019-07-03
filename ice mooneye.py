tom = Turtle()
tom.shape('turtle')
tom.color('light blue')
tom.tracer(100)


for count in range(100):
    for count in [1,2,3,4]:
        tom.fd(100)
        tom.rt(60)
        tom.fd(100)
        tom.rt(170)
        tom.fd(100)
        tom.rt(60)
        tom.fd(100)

tom.goto(-61,110)
tom.color('white')
        
for count in range(100):
    for count in [1,2,3,4]:
        tom.fd(50)
        tom.rt(60)
        tom.fd(50)
        tom.rt(170)
        tom.fd(50)
        tom.rt(60)
        tom.fd(50)
    
    tom.rt(360.0/100)
tom.penup()
tom.lt(360)
