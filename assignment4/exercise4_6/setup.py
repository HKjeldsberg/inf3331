from distutils.core import setup
name='mandelbrot_1'

setup(name=name,
      version='0.1',
    py_modules=[name],       # modules to be installed
    scripts=[name + '.py'],  # programs to be installed
)
