import numpy as np
import matplotlib.pyplot as plt
import time
import mandelbrot

# Parameters
maxiter = 50
dim = 1000
size = dim*dim
xmin = -2; xmax = 0.5;
ymin = -1.25; ymax = 1.25;

# Compute using SWIG module
t0 = time.clock()
values = mandelbrot.compute_mandelbrot(xmin,xmax,ymin,ymax,maxiter,dim, size)
t1 = time.clock()
diff  = t1 - t0
print("Time to compute using using n=%i points is t=%.5f" % (dim, diff))

# Plot Mandelbrot set
values2 = np.reshape(values, (dim, dim ))
plt.imshow(values2.T, extent=[xmin,xmax,ymin,ymax], cmap='hot')
plt.show()


    





    

