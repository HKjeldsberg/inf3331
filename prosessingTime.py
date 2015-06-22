import time
n = int(1e8)
print "n = %g \n" % n

"""
Compare range and xrange
"""


realtime = time.time()
cputime = time.clock()
for i in xrange(n):
    pass
t0 = time.time() - realtime
cpu_t0 = time.clock() - cputime
print "xrange:"
print t0,"seconds"
print "CPU",cpu_t0,"seconds"


realtime = time.time()
cputime = time.clock()
for i in range(n):
    pass
t0 = time.time() - realtime
cpu_t0 = time.clock() - cputime
print"\nrange:"
print t0,"seconds"
print "CPU:",cpu_t0,"seconds"
