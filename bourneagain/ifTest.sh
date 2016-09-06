# the 'then' statement can appear on 1st line
dir=$1
if [ -d $dir ]; then
    echo "This is a directory!"
fi


# Another if test
if test -d $dir; then
    echo "This is still a directory!"
fi

#Third 
test -d $dir && echo "This is clearly a directory!"



