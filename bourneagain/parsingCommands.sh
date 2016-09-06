while [ $# -gt 0 ]
do 
    option = $1;
    shift;
    case "$option" in
        -m)
            m=$1;shift; ;;
        -b)
            b=$1; shift; ;;
        *)
            echo "$0: invalid option \"$option\""; exit ;;
    esac
done
