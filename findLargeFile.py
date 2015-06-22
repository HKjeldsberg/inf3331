import os

def checksize(arg,dirname,files):
    for fil in files:
        # construct the file's complete path
        filename = os.path.join(dirname,fil)
        if os.path.isfile(filename):
            size = os.path.getsize(filename)
            if size > 1e10:
                print "%.2fMb %s" % (size/1.e10,filename)

root = os.environ['HOME']
os.path.walk(root,checksize,None)


