import turtle as t
t.speed("fastest")
t.bgcolor('black')

n1 = 0
n2 = 1

for i in range(20):
    fibo = n1 + n2
    t.pencolor('white')

    for j in range(6):
        t.fd(fibo)
        t.lt(90)
    t.rt(90)
    n1 = n2
    n2 = fibo

t.done()