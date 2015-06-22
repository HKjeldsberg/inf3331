import time,glob,tarfile,os,sys
# Files to compress
files = glob.glob('*.py')
print files
tar = tarfile.open('pyfiles.tar.gz','w:gz') # gzip compression

# Add files to compress
for i in files:
    tar.add(i)



# Check contents
members = tar.getmembers()
for info in members:
    print '%s: size=%d, mode=%s, mtime=%s' % (info.name,info.size,info.mode,time.strftime('%Y.%m.%d',time.gmtime(info.mtime)))

# Close tar
tar.close()
