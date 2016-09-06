#!/bin/bash

# FORSKNINGSPARKEN
furl='https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0'
# BLINDERN
burl='https://ruter.no/reiseplanlegger/Stoppested/(3010360)Blindern%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0'
# ULLEVÅL
uurl='https://ruter.no/reiseplanlegger/Stoppested/(3012210)Ullev%C3%A5l%20stadion%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0'

# Blindern
if [ "$1" = "Blindern" ]; then
  echo "Departure times from Blindern"
  echo "-----------------------------"
  STATION="$(curl -Ls $burl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination.{0,40}' | cut -d"\"" -f3 )"
  TIME="$(curl -Ls $burl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'remainingMinutes.{0,10}' | grep -o '[0-9]*')"

# Ullevål
elif [ "$1" = "Ullevål" ]; then
  echo "Departure times from Ullevål"
  echo "----------------------------"
  STATION="$(curl -Ls $uurl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination.{0,40}' | cut -d"\"" -f3 )"
  TIME="$(curl -Ls $uurl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'remainingMinutes.{0,10}' | grep -o '[0-9]*')"
# Forskningsparken
else 
  echo "Departure times from Forskningsparken"
  echo "-------------------------------------"
  STATION="$(curl -Ls $furl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination.{0,40}' | cut -d"\"" -f3 )"
  TIME="$(curl -Ls $furl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'remainingMinutes.{0,10}' | grep -o '[0-9]*')"
fi

STAT=${STATION// via /-via-}

# Create array of departure times
declare -a UPCOMING
declare -a STATIONS
declare -i k=0

for j in $TIME; do
  UPCOMING[$k]=$j
  ((k++))
done

k=0
for j in $STAT; do
  STATIONS[$k]=$j
  ((k++))
done

declare i n=0
# Check west or east 
if [ "$2" = "--E" ]; then
   for i in `seq 0 2`; do
      time=${UPCOMING[(( $i * 5))]}
      place=${STATIONS[$i]}
      echo "Departure to $place in $time minutes"
   done    
				    
elif [ "$2" = "--W" ]; then
   for i in `seq 3 5`; do
     time=${UPCOMING[(( $i * 5))]}
      place=${STATIONS[$i]}
     echo "Departure to $place in $time minutes"
   done    

else
  for i in $STAT; do
    time=${UPCOMING[(( $n * 5))]}
    echo "Departure to $i in $time minutes"
    ((n++))
  done
fi

