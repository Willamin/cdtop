cdtop
=====

Something like 
```
function cdtop()
{
    VAR=$(python ~/Documents/python/cdtop/cdtop.py "$1")
    if [ "$VAR" = "." ]
    then
        echo "No parent found"
    else
        cd $VAR
    fi
}
```
must be added to bash profile. Keep in mind that you should change the path to `cdtop.py` accordingly.

For reference, I also added this alias to my bash profile: ```alias cdm='cdtop .modman; cd *'```. This allows me to jump to the "root" directory of a modman'd site.
