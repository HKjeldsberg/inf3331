import numpy as np
import matplotlib.pyplot as plt
import time
import mandelbrot

n_values = [1000]#[100,250,500,750,1000,2000]
maxiter = 50
size = n_values[0]*n_values[0]
xmin = -2; xmax = 0.5;
ymin = -1.25; ymax = 1.25;
for n in n_values:
    t0 = time.clock()
    values = compute_mandelbrot(xmin,xmax,ymin,ymax,maxiter,size)
    print values
    t1 = time.clock()
    diff  = t1 - t0
    print("Time to compute using n=%i is t=%.5f" % (n, diff))



    





    

