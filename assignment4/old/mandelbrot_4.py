import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import weave

def compute_mandelbrot(c, maxiter):
    z = 0
    for n in range(maxiter):
        z = z**2 + c
        if abs(z) > 2:
            return n

    return 0

def compute_mandelbrot_weave(c, maxiter):
    code = """
    #include <math.h>
    #include <complex>
    std::complex<double> z = 0;
    int value = 0;
    bool diverge = false;
    for (int n=0; n < maxiter; n++){
        z = std::pow(z,2) + c;
        if (std::abs(z) > 2){
            value =  n;
            diverge = true;
            break;
        }
    }
    if (diverge){
        return_val = value;
    }
    else{
        return_val = 2;
    }
    """
    return weave.inline(code,['c','maxiter'])

def mandelbrot_python(xmin, xmax, ymin, ymax, maxiter, n):
    dx = (xmax - xmin)/float(n)
    dy = (ymax - ymin)/float(n)
    x = []
    y = []
    for i in range(n):
        x.append(xmin + dx*i)
        y.append(ymin + dy*i)

    values = [[0 for i in range(n)] for j in range(n)]
    for i, x_ in enumerate(x):
        for j, y_ in enumerate(y):
            values[j][i] = compute_mandelbrot(complex(x_,y_),  maxiter)


    return values

def mandelbrot_weave(xmin, xmax, ymin, ymax, maxiter, n):
    
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(ymin, ymax, n)
    values = np.zeros((n,n))
    
    for i, x_ in enumerate(x):
        for j, y_ in enumerate(y):
            values[j,i] = compute_mandelbrot_weave(complex(x_,y_),  maxiter)

    return values


def mandelbrot_numpy(xmin, xmax, ymin, ymax, maxiter, n):
    
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

        t0 = time.clock()
        values = mandelbrot_weave(xmin, xmax, ymin, ymax, maxiter, n)
        t1 = time.clock()
        t_weave = t1 - t0
        
        print("n = %i" % n)
        print("Runtime using Python (%i points): %.4f seconds" % (n**2, t_python))
        print("Runtime using Numpy (%i points): %.4f seconds" % (n**2, t_numpy))
        print("Runtime using weave (%i points):  %.4f seconds" % (n**2, t_weave))

    # Plot
    plot(values, xmin,xmax,ymin,ymax)

def plot(values, xmin, xmax, ymin, ymax):
    plt.title("Plot of mandelbrot set in the complex plane")
    plt.imshow(values, cmap = plt.cm.hot ,extent = (xmin,xmax,ymin,ymax))
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.show()

if __name__ == '__main__':
    n_values=[1000]#n_values = [100,250,500,750,1000,2000]
    maxiter = 100
    xmin = -2; xmax = 0.5;
    ymin = -1.25; ymax = 1.25;
    compare_runtime(n_values, xmin, xmax, ymin, ymax, maxiter)



    

