#!/bin/sh
for i in $@; 
do 
    echo "Unpacking file $i"
    echo "cat > $i <<EOF"
    cat $i
    echo "EOF"
done
