#!/bin/bash

BASE=`dirname $0`

if [ "$1" == "push" ] ; then
    pushd .
    cd $BASE
    cp -r docs/home/* .
    git commit -a -m "Updates...."
    git push 
    popd
    exit
fi

cat > $BASE/docs.html <<EOF
<div id="sphinx-docs">
 <ul>
EOF

for i in $BASE/src/* ; do
    cd $i;
    make html; 
    cd ..;
    DOC=`basename $i`;
    echo "**** $i > $BASE/docs/`basename $i`";
    if [ ! -d $BASE/docs/$DOC ] ; then
        mkdir -p $BASE/docs/$DOC ;
    fi;
    echo "cp -r $i/build/html/* $BASE/docs/$DOC";
    cp -r $i/build/html/* $BASE/docs/$DOC;
    git add $BASE/docs/$DOC ;
    cat >> $BASE/docs.html << EOF
    <li><a href="docs/$DOC/">$DOC</a></li>
EOF
done

cat >> $BASE/docs.html <<EOF
  </ul>
</div>
EOF

