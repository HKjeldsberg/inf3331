import time,sys,numpy as np

def timer(func,args,kwargs,iters,name):
    t0 = time.time(); c0 = time.clock();

    for i in xrange(iters):
        func(*args,**kwargs)

    print "%s: elapsed=%g, CPU=%g" % (name,time.time()-t0,time.clock()-c0)

def f(*x,**func):
    for x_ in x:
        for f_name, f_ in func.items():
            f_(x_)

n = int(sys.argv[1])
mylist = [0.5,0.8,1.3,1.5]
mydict = {'sin':np.sin, 'cos': np.cos,'exp':np.exp}
# Test timer
timer(f,mylist,mydict,n,"Math functions")
# Test function
f(*[0,0.5,0.5],**{'cos':np.cos})
