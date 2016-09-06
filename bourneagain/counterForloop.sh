declare -i n;
n=0
# Arithmetic inside (( ))
for arg in $@; 
do 
    # Print argument 
    echo "Commandline arg no.$n = <$arg>"

    # Increment counter
    ((n++))
done
