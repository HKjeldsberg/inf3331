#!/bin/sh
r=$1
s=`echo "$r+$r + s($r) + c($r) + e($r)" | bc -l`
echo "$r + $r + sin($r) + cos($r) + exp($r) = $s"
