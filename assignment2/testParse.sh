
while read -r a b line
do
      [[ $line =~ ([0-9]+)pts$ ]] && echo "$a $b, ${BASH_REMATCH[1]}"
done < test.txt
