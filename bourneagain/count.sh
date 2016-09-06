declare -i counter
counter=0
# Arithmetic inside (( ))
((counter++))
echo $counter # Prints 1
