# compute something
#!/bin/sh
function calc() {
echo "
if ( $1 >= 0.0 ) {
    ($1)^5*e(-($1))
} else {
0.0
} " | bc -l
}
r=4.2
s=`calc $r`
