cdtop
=====

Something like 
```function cdtop()
{
    VAR=$(python ~/Documents/python/cdtop/cdtop.py "$1")
    if [ "$VAR" = "." ]
    then
        echo "No parent found"
    else
        cd $VAR
    fi
}```
must be added to bash profile.