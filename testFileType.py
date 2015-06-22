import time,os.path,glob,sys
myfiles = glob.glob('*.py')
# Index of files from commandline
index = int(sys.argv[1])
myfile = myfiles[index]
print myfile,

# Check file type
if os.path.isfile(myfile):
    print 'is a plain file'
if os.path.isdir(myfile):
    print 'is a folder'
if os.path.islink(myfile):
    print 'is a a link'

# Check file size and age
size = os.path.getsize(myfile)
print "Size:", size, "byte"

access_date = os.path.getatime(myfile)
mod_date = os.path.getmtime(myfile)

days_access = (time.time() - access_date)/(3600.*24)

print "Days:",days_access


# Stat module
import stat
mystat = os.stat(myfile)
filesize = mystat[stat.ST_SIZE]
print "Size (stat):",filesize, "bytes"
