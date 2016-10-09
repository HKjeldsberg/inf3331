%module example 
%{
/* Put header files here and functon declarations below*/
extern double compute_mandelbrot(double _Complex c, int maxiter);
%}

extern double compute_mandelbrot(double _Complex c, int maxiter);
