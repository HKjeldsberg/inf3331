import mandelbrot_1

def test_outside():
    xmin = 3
    xmax = 4
    ymin = 3
    ymax = 4
    Nx = 750
    Ny = 750
    max_escape_time = 100
    values = mandelbrot_1.compute_mandelbrot(xmin,xmax,ymin,ymax, Nx, Ny, max_escape_time )
    
    # Check if mandelbrot set is entirely outside
    assert values.max() == 0

def test_inside():
    xmin = -0.5
    xmax = 0.1
    ymin = -0.25
    ymax = 0.25
    Nx = 750
    Ny = 750
    max_escape_time = 100

    values = mandelbrot_1.compute_mandelbrot(xmin,xmax,ymin,ymax, Nx, Ny, max_escape_time )
    
    # Check if mandelbrot set is entrely inside 
    assert values.max() == 0

test_outside()
test_inside()

    
