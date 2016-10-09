#include <math.h>
#include <complex.h>
#include <stdio.h>
#include "mandelbrot.h"

void compute_mandelbrot(double xmin, double xmax, double ymin, double ymax,  int maxiter, int size2, int size,int *values){

    double complex z;
    double complex c;
    double dx, dy;
    double x,y;
    int n;
    int i, j;

    dx = (xmax - xmin)/size2;
    dy = (ymax - ymin)/size2;
    i  = 0;
    for (x = xmin; x < xmax; x+=dx){
        j = 0;
        for (y = ymin; y < ymax; y += dy){
            z = 0;
            c = x + y*I;
            n = 0;
            while (cabs(z) < 2 && n < maxiter){
                z = cpow (z, 2) + c;
                n++;
            }
            if (i != size2){
                if (n == maxiter){
                    values[i*size2 + j] = 0;
                }
                else{
                    values[i*size2 + j] = n; 
                }
            }

            j++;

        }   
        i++;
    }
}

