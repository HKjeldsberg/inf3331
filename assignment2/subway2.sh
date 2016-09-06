#!/bin/bash
#
#curl -s http://www.yr.no/place/Norway/Oslo/Oslo/Oslo/ | grep  "forskningsparken"

# FORSKNINGSPARKEN
furl='https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0'
# BLINDERN
burl='https://ruter.no/reiseplanlegger/Stoppested/(3010360)Blindern%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0'
# ULLEVÅL
uurl='https://ruter.no/reiseplanlegger/Stoppested/(3012210)Ullev%C3%A5l%20stadion%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0'

FORSK="$(curl -gs $furl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"
BLIND="$(curl -gs $burl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"
ULLEV="$(curl -gs $uurl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"

echo $BLIND
INFO=$(echo $BLIND | tr "," "\n")
echo $INFO
INFOCUT=$(echo $INFO | tr "departureTime\"" "\n")
echo $INFOCUT
define -a TIME0
define -i n=0

for addr in $INFO
do
      echo " $addr"
      TIME0[$n]=$addr
      ((n++))
done

# 
define -i m=1
define -a TIME
for i in `seq 0 5`;
do
    TIME[$i]=${TIME0[((4 + 9*$i))]%\"*}
    TIME[$i]=${TIME[$i]##*\"}
    echo ${TIME[$i]}
    ((m++))
done    
#echo ${TIME[0]}
#echo ${TIME[1]}
#TIME=${TIME0[4]%\"*}
#TIME=${TIME##*\"}
echo $TIME
