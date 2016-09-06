#!/bin/sh
r=$1
s=$2
cat > myfile <<EOF
This is my text
and here are
some numbers
1: $r
2: $s
End of text.
EOF

