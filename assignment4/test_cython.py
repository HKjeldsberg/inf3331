import mandelbrot_cython
import matplotlib.pyplot as plt

# Parameters
maxiter = 50
n = 1000
xmin = -2; xmax = 0.5;
ymin = -1.25; ymax = 1.25;

# Compute using SWIG module
values = mandelbrot_cython.main(xmin,xmax,ymin,ymax,maxiter,n)

# Plot Mandelbrot set
plt.imshow(values, extent=[xmin,xmax,ymin,ymax], cmap='hot')
plt.show()


    





    

