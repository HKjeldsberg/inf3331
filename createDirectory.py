import glob,sys,os
dirname = sys.argv[1]
if not os.path.isdir(dirname):
    os.mkdir(dirname)
os.chdir(dirname)
