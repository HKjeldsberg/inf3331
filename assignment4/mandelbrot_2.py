import numpy as np
import matplotlib.pyplot as plt
import time

def mandelbrot_python(c, maxiter):
    z = 0
    for n in range(maxiter):
        z = z**2 + c
        if abs(z) > 2:
            return n

    return 0

def mandelbrot_numpy(z, maxiter):
    output = np.zeros(z.shape, dtype=np.int32)
    c = z.copy()
    for n in range(maxiter):
        output += np.abs(z) < 2
        z *= z
        z += c
        
    return output

def mandelbrot_py(xmin, xmax, ymin, ymax, maxiter, n):
    dx = (xmax - xmin)/float(n)
    dy = (ymax - ymin)/float(n)
    x = []
    y = []
    for i in range(n):
        x.append(xmin + dx*i)
        y.append(ymin + dy*i)

    values = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(x)):
        for j in range(len(y)):
            values[j][i] = mandelbrot_python(x[i] + 1j*y[j],  maxiter)

    return values

def mandelbrot_num(xmin, xmax, ymin, ymax, maxiter, n):
    
    x,y = np.meshgrid(np.linspace(xmin, xmax, n), np.linspace(ymin,ymax,n))
    z = x + y*1j
    values = mandelbrot_numpy(z, maxiter)
    return values

def compare_runtime(n_values, xmin, xmax, ymin, ymax, maxiter):

    for n in n_values:
        # Compute mandelbrot values

        t0 = time.clock()
        values = mandelbrot_py(xmin, xmax, ymin, ymax, maxiter, n)
        t1 = time.clock()
        t_python = t1 - t0

        t0 = time.clock()
        values = mandelbrot_num(xmin, xmax, ymin, ymax, maxiter, n)
        t1 = time.clock()
        t_numpy = t1 - t0


        print("Runtime using numpy (%i points):  %.4f seconds" % (n**2, t_numpy))
        print("Runtime using Python (%i points): %.4f seconds" % (n**2, t_python))




if __name__ == '__main__':
    n_values = [1000]#[100,250,500,750,1000,2000]
    maxiter = 50
    xmin = -2; xmax = 1.5;
    ymin = -1.25; ymax = 1.25;

    compare_runtime(n_values, xmin, xmax, ymin, ymax, maxiter)


    




