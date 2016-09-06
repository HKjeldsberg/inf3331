#!/bin/bash
#
#curl -s http://www.yr.no/place/Norway/Oslo/Oslo/Oslo/ | grep  "forskningsparken"

# FORSKNINGSPARKEN
furl='https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0'
# BLINDERN
burl='https://ruter.no/reiseplanlegger/Stoppested/(3010360)Blindern%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0'
# ULLEVÅL
uurl='https://ruter.no/reiseplanlegger/Stoppested/(3012210)Ullev%C3%A5l%20stadion%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0'


#curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' 
#BERG="$(curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep  -m 1 "Retning" )"
#echo $BERG

BERG="$(curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep -m 1 "Bergkrystallen" | cut -d"{" -f9,10| cut -d"\"" -f10 )"
TIME="$(curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep -m 1 "Bergkrystallen" | cut -d"{" -f10,10 | cut -d"\"" -f11,14 | cut -d "\"" -f2)"
#echo "Next departures to" $BERG "is": $TIME

FORSK="$(curl -gs $furl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"
#echo $FORSK

BLIND="$(curl -gs $burl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"
#echo $BLIND

ULLEV="$(curl -gs $uurl | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"
#echo $ULLEV

BERG0="$(curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep -m 1 "Bergkrystallen" | grep -o -E -e 'destination'.{36} -e  'departureTime.{10}')"
#BERG2="$(curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep -m 1 "Bergkrystallen" | cut -d"{" -f22 )"
#echo $BERG2

#BERG="$(curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep -m 1 "Bergkrystallen")"
#echo $BERG

#curl -gs 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d/Avganger/#st:1,sp:0,bp:0' | grep -m 1 "Vestli" | cut -d"{" -f10

#cut  "\{" f4 index.html 
#echo $a
#curl -l -s #lin # grep -o -E -e 'departureTime
#curl | grep -o -E -e 'departureTime":",.{5}' -e 'destination":".{35}' -e 'Retning' | cut -d"\"" - f3

#IN=$BERG0

INFO=$(echo $BERG0 | tr "," "\n")
#define -a AREA
#define -i n=0


for addr in $INFO
do
      AREA[$n]=$addr
      echo $addr
      ((n++))
done
echo " #########################################"
echo " Upcoming departures from Forskningsparken"
echo " #########################################"
a=${AREA[0]##*\"}
b=${AREA[1]} 
c=${AREA[2]%\"}
TIME=${AREA[4]%\"*}
TIME=${TIME##*\"}
echo " $a $b $c: $TIME"

a=${AREA[9]##*\"}
b=${AREA[10]} 
c=${AREA[11]%\"}
TIME=${AREA[13]%\"*}
TIME=${TIME##*\"}
echo " $a $b $c: $TIME"

a=${AREA[18]##*\"}
b=${AREA[19]} 
c=${AREA[20]%\"}
TIME=${AREA[22]%\"*}
TIME=${TIME##*\"}
echo " $a $b $c: $TIME"

a=${AREA[27]##*\"}
b=${AREA[28]} 
c=${AREA[29]%\"}
TIME=${AREA[31]%\"*}
TIME=${TIME##*\"}
echo " $a $b $c: $TIME"

a=${AREA[36]##*\"}
#a=$a%\"
TIME=${AREA[39]%\"*}
TIME=${TIME##*\"}
echo " $a : $TIME"

a=${AREA[44]##*\"}
b=${AREA[45]} 
c=${AREA[46]%\"}
TIME=${AREA[48]%\"*}
TIME=${TIME##*\"}
echo " $a $b $c: $TIME"
#TIME=${AREA[4]%\"*}
#TIME=${TIME##*\"}
#echo $NAME
