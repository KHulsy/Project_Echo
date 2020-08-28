Disclaimer: This is 100 percent not my code. This is a snippet I found which 1. makes me happy 2. gives me project inspiration in the capacity of positive reinforcement.
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()
def branch():
for i in range(3):
    for i in range(3):
        elsa.forward(30)
        elsa.backward(30)
        elsa.right(45)
    elsa.left(90)
    elsa.backward(30)
    elsa.left(45)
elsa.right(90)
elsa.forward(90)
for i in range(8):
    branch()
    elsa.left(45)
