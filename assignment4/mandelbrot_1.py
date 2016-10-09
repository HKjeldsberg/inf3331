import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(c, maxiter):
    z = 0
    for n in range(maxiter):
        z = z**2 + c
        if abs(z) > 2:
            return n

    return 0

def mandelbrot(xmin, xmax, ymin, ymax, maxiter, n=1000):
    
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(ymin, ymax, n)
    values = np.zeros((len(y),len(x)))
    for i, x_ in enumerate(x):
        for j, y_ in enumerate(y):
            values[j,i] = compute_mandelbrot(complex(x_,y_),  maxiter)

    return values

def plot(values, xmin, xmax, ymin, ymax):
    plt.title("Plot of mandelbrot set in the complex plane")
    plt.imshow(values, cmap = plt.cm.gist_stern,extent = (xmin,xmax,ymin,ymax))
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.show()


if __name__ == '__main__':

    maxiter = 100
    xmin = -2; xmax = 0.5;
    ymin = -1.25; ymax = 1.25;

    # Compute mandelbrot values
    values = mandelbrot(xmin, xmax, ymin, ymax, maxiter)

    # Plot
    plot(values, xmin,xmax,ymin,ymax)


    




