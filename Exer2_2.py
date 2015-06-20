# Draw n random numbers and print average m times
import random,sys,numpy as np
try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except:
    print "Usage: %s #numbers #iterations" % sys.argv[0]
    sys.exit(0)

for i in range(m):
    num = np.random.uniform(5,10,n)
    avg = np.sum(num)/n
    print avg
