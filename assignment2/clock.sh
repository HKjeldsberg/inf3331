#!/bin/bash

if [ "$1" = '--AMPM' ]; then
    while true; do
	date +'%r'

	sleep 1
	clear
    done

else 
    while true; do
	date +'%T'
	sleep 1
	clear
    done
fi 
