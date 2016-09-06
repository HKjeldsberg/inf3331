#!/bin/bash

if [ "$1" = '--AMPM' ]; then
    while true; do
        HOUR=$(date +"%H")
	echo $
	if [ $HOUR < 11 ]; then
	    #date +'%r' 
	    echo $HOUR
	    sleep 1
	    clear
	else
	    date +'%r' 
	    sleep 1
	    clear
	fi

    done

else 
    while true; do
	date +'%T'
	sleep 1
	clear
    done
fi 
