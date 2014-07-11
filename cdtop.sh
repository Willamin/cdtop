#!/bin/bash
VAR=`python ~/Documents/python/cdtop/cdtop.py $1`
if [ "$VAR" = "." ]
then
    echo "No parent found"
else
    cd $VAR
fi