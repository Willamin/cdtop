#!/bin/bash
VAR=`python ~/Documents/python/cdtop/cdtop.py`
if [ "$VAR" = "." ]
then
    echo "No parent found"
else
    cd $VAR
fi