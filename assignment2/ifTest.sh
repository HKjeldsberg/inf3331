#!/bin/bash

# Declare number variable
declare -i n=0

# Summation 
if [ "$1" = "S" ]; then
    shift
    while [ $# -gt 0 ]
    do 
	n=$(( n+$1 )) 
	shift;
    done
fi

# Product of numbers
if [ "$1" = "P" ]; then
    shift
    n=$1
    shift
    while [ $# -gt 0 ]
    do 
	n=$(( $n*$1 )) 
	shift;
    done
fi

# Find maximum
if [ "$1" = "M" ]; then
    shift
    n=$1
    shift
    while [ $# -gt 0 ]
    do 
	if [ $1 -gt $n ]; then
	    n=$1
	fi
	shift;
    done
    
fi

# Find minimum
if [ "$1" = "m" ]; then
    shift
    n=$1
    shift
    while [ $# -gt 0 ]
    do 
	if [ $1 -lt $n ]; then
	    n=$1
	fi
	shift;
    done
fi

echo "$n"
