import turtle

bob = turtle.Turtle()
print(bob)

bob.color("blue","red")
# move

for i in range(4):
    bob.fd(100)
    bob.lt(90)

# bob.lt(50) #angle
# bob.fd(100)
# bob.rt(100)
# bob.fd(100)
# bob.begin_fill()
# bob.circle(200)
# bob.end_fill()

turtle.done()
