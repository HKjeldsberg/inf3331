# Declare counter
declare -i i;
# Declare limit
declare -i n; n=$1

for ((i=0; i<=$n; i++));
do 
    echo "Counter is $i"
done
