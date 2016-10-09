from distutils.core import setup, Extension
import numpy
import os

setup(name='mandelbrot',
    version='1.0',
    ext_modules =[Extension('_mandelbrot',
     ['mandelbrot.c', 'mandelbrot.i'],
    include_dirs = [numpy.get_include(),'.'])
])
