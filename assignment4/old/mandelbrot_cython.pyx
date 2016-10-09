import time
import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(c, maxiter):
    z = 0
    for n in range(maxiter):
        z = z**2 + c
        if abs(z) > 2:
            return n

    return 0

def mandelbrot_python(xmin, xmax, ymin, ymax, maxiter, n):

    """
    dx = (xmax - xmin)/float(n)
    dy = (ymax - ymin)/float(n)
    x = []
    y = []
    for i in range(n):
        x.append(xmin + dx*i)
        y.append(ymin + dy*i)
    """

    import numpy as np
    x = np.linspace(xmin, xmax, n).tolist()
    y = np.linspace(ymin, ymax, n).tolist()
    values = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(x)):
        for j in range(len(y)):
            #values[j][i] = compute_mandelbrot(complex(x[i],y[j]),  maxiter)
            values[j][i] = compute_mandelbrot(x[i] + 1j*y[j],  maxiter)


    return values

def mandelbrot_numpy(xmin, xmax, ymin, ymax, maxiter, n):
    
    import numpy as np
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(ymin, ymax, n)
    values = np.zeros((n,n))
    
    for i, x_ in enumerate(x):
        for j, y_ in enumerate(y):
            values[j,i] = compute_mandelbrot(complex(x_,y_),  maxiter)

    return values

def compare_runtime(n_values, xmin, xmax, ymin, ymax, maxiter):


    for n in n_values:
        # Compute mandelbrot values
        t0 = time.clock()
        values = mandelbrot_numpy(xmin, xmax, ymin, ymax, maxiter, n)
        t1 = time.clock()
        t_numpy = t1 - t0

        t0 = time.clock()
        values = mandelbrot_python(xmin, xmax, ymin, ymax, maxiter, n)
        t1 = time.clock()
        t_python = t1 - t0

        print("Runtime using numpy (%i points):  %.4f seconds" % (n**2, t_numpy))
        print("Runtime using Python (%i points): %.4f seconds" % (n**2, t_python))


def main():

    n_values = [1000]#[100,250,500,750,1000,2000]
    maxiter = 50
    xmin = -2; xmax = 0.5;
    ymin = -1.25; ymax = 1.25;

    compare_runtime(n_values, xmin, xmax, ymin, ymax, maxiter)


    




