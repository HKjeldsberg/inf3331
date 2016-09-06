#!/bin/sh
r=$1 # Store value

# Method of using math function
s=`echo "s($r)" | bc -l`
# print to screen
echo "Hello,World! sin($r) = $s"
