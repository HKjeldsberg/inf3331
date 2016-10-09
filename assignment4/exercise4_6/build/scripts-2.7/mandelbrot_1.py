import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_escape_time):
    z = 0
    for n in range(max_escape_time):
        z = z**2 + c
        if abs(z) > 2:
            return n

    return 0

def init_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time):
    
    x = np.linspace(xmin, xmax, Nx)
    y = np.linspace(ymin, ymax, Ny)
    values = np.zeros((len(y),len(x)))
    for i, x_ in enumerate(x):
        for j, y_ in enumerate(y):
            values[j,i] = mandelbrot(complex(x_,y_),  max_escape_time)

    return values

def plot(values, xmin, xmax, ymin, ymax,plot_filename):
    plt.title("Plot of mandelbrot set in the complex plane")
    plt.imshow(values, cmap = plt.cm.hot ,extent = (xmin,xmax,ymin,ymax))
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.show()
    if plot_filename != None:
        plt.savefig("%s.png" % plot_filename)
        print("Plot was saved in file: %s.png" % plot_filename)


def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, plot_filename=None):

    # Compute mandelbrot values
    values = init_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)

    # Plot
    plot(values, xmin,xmax,ymin,ymax,plot_filename)

    return values


    




