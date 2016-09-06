#!/usr/bin/env python
import sys, math
a = float(sys.argv[1])
s = math.sin(a)
print "Hello World! sin(%g) = %.2f" % (a,math.sin(a))
print "Hello World! sin(%(a)g) = %(s)g" % vars()
print "Hello World! sin(%(a)g) = %(s)12.5e" % vars()
