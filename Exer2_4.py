# Print natural log of numbers from command line
#! /usr/bin/env python
from math import log
import sys

def print_ln(x):
    if x <= 0:
        print "ln(%g) is illegal" % x
    else:
        print "ln(%g) = %g" % (x,log(x))


for i in sys.argv[1:]:
    try:
        print_ln(float(i))
    except:
        print "Value must be a number"
        sys.exit(0)

