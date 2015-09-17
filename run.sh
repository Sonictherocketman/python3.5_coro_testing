#! /bin/bash
# Get the results from each test set.

for dir in */;
do
    echo "====> $dir <===="
    for py in `ls $dir*py`;
    do
        echo $py
        echo "--------" 
        time python3.5 $py
    done
done
rm *.dat
