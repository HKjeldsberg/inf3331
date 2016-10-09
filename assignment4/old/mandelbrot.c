#include <math.h>
#include <complex.h>


double compute_mandelbrot(double _Complex c, int maxiter){

    double _Complex z = 0;
    int value = 0;
    int  diverge = 0;
    int n;
    for (n=0; n < maxiter; n++){
        z = cpow (z, 2) + c;
        if (cabs(z) > 2){
            value =  n;
            diverge = 1;
            break;
        }
    }
    if (diverge == 1){
        return value;
    }
    else{
        return 2;
    }
}
