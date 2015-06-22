#!/bin/sh
r=$1 # Store value
s='echo "s($r)" | bc -l'
echo "Hello, World! sin($r) =$s"
echo "Hello, World! cos($r) = $(echo "c($r)" | bc -l)"
