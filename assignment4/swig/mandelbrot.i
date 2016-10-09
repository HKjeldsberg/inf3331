/* file: mandelbrot.i */
%module mandelbrot

/* Put header files here and functon declarations below*/
%{
#define SWIG_FILE_WITH_INIT
#include "mandelbrot.h"
%}

%include "numpy.i"
%init %{
import_array();
%}

%apply (int DIM1, int* ARGOUT_ARRAY1){(int size, int *values)};
%include "mandelbrot.h"
