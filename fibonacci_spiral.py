import turtle as t
n1, n2 = 0, 1
fibo = None

for i in range(20):
    fibo = n1 + n2
    t.circle(fibo, 180)

    n1 = n2
    n2 = fibo
