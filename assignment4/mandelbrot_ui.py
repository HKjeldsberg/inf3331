import mandelbrot_1
import mandelbrot_2
import mandelbrot_cython
import sys
import matplotlib.pyplot as plt

def menu():
    try: 
        xmin = float(raw_input("Minimum x value: "))
        xmax = float(raw_input("Maximum x value: "))
        ymin = float(raw_input("Minimum y value: "))
        ymax = float(raw_input("Maximum y value: "))
        maxiter = int(raw_input("Number of iterations per number: "))
        n = int(raw_input("Dimension of x and y arrays: "))
    except ValueError:
        print("Value must be a number!")

    filename = raw_input("Filename to save plot into: ")
    return xmin, xmax, ymin, ymax, maxiter, n, filename

# Plot method for plotting the mandelbrot set
def plot(values, xmin, xmax, ymin, ymax, filename, show):
    plt.title("Plot of mandelbrot set in the complex plane")
    plt.imshow(values, cmap = plt.cm.hot ,extent = (xmin,xmax,ymin,ymax))
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.savefig("%s.png" % filename)
    print("Plot was saved to file: %s.png" % (filename))

    if show == 'yes' or show == 'y':
        plt.show()

while True:
    
    try: 
        arg = sys.argv[1]
    except IndexError:
        print("Usage (1): python mandelbrot_ui.py 1 OR 2 OR 3")
        print("Usage (2): python mandelbrot_ui.py --help")
        sys.exit(1)
    
    if arg == '--help':
        xmin,xmax,ymin,ymax, maxiter, n, filename = menu() 
        imp = raw_input("\nSelect implementation: \n Mandelbrot using Python = 1\n Mandelbrot using Numpy = 2 \n Mandelbrot using Cython = 3\n>>")

    elif arg == '1' or arg == '2' or arg =='3': 
        xmin, xmax, ymin, ymax, maxiter, n, filename = menu()
        imp = arg
    
    else:
        print("Usage (1): python mandelbrot_ui.py 1 OR 2 OR 3 ")
        print("Usage (2): python mandelbrot_ui.py --help")
        sys.exit(1)

    show = raw_input("Do you want to plot the figure? (y/n) ")
    
    # Select implementation
    if imp == '1':
        values = mandelbrot_1.mandelbrot(xmin,xmax,ymin,ymax,maxiter,n)
    elif imp == '2':
        values = mandelbrot_2.mandelbrot_num(xmin,xmax,ymin,ymax, maxiter, n)
    elif imp == '3':
        values = mandelbrot_cython.mandelbrot_cython(xmin,xmax,ymin,ymax,maxiter,n)
    else:
        print("No valid implementation selected. Program will exit.")
        sys.exit(1)

    # Create plot 
    plot(values,xmin,xmax,ymin,ymax, filename,show)

    print("\nNext simulation:\n")





