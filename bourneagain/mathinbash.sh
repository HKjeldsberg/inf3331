r=$1
echo $r
s=`echo "s($r)" | bc -l`
echo $s

s = $(echo ´s($r)´ | bc -l´)
