x = [i for i in range(5)]
def f(x):
    p = x+1
    p[10] = 0
    return p

x = f(x)
