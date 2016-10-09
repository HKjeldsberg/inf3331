import numpy as np
cimport numpy as np
import time

def compute_mandelbrot(c, maxiter):
    # Declare variables
    cdef int n
    cdef double complex z

    z = 0
    for n in range(maxiter):
        z = z*z + c
        if abs(z) > 2:
            return n

    return 0


def mandelbrot_cython(xmin, xmax, ymin, ymax, maxiter, n):
    
    cdef np.ndarray[double, ndim=1] x = np.linspace(xmin, xmax, n)
    cdef np.ndarray[double, ndim=1] y = np.linspace(ymin, ymax, n)

    cdef np.ndarray[double, ndim=2] values = np.zeros((n,n))

    # Declare integers
    cdef int i,j

    # Declare doubles
    cdef double x_, y_

    for i, x_ in enumerate(x):
        for j, y_ in enumerate(y):
            values[j,i] = compute_mandelbrot(complex(x_,y_),  maxiter)

    return values

def main(xmin,xmax,ymin,ymax,maxiter, n):
    t0 = time.clock()
    values = mandelbrot_cython(xmin,xmax,ymin,ymax,maxiter,n)
    t1 = time.clock()
    diff  = t1 - t0
    print("Time to compute using n=%i is t=%.5f" % (n, diff))
    return values



    




