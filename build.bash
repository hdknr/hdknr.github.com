#!/bin/bash

for i in src/* ; do
    echo "$i > docs/`basename $i`";
    if [ ! -d docs/`basename $i` ] ; then
        mkdir -p docs/`basename $i`;
    fi;
    cp -r $i/build/html/* docs/`basename $i`;
    git add docs/`basename $i`;
done
git commit -a -m "Updates...."
#git push
