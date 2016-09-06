#!/bin/sh 

r=$1
s=`echo "c($r)" | bc -l`
printf "Hello, World! cos(%g) = %.4f \n" $r $s
