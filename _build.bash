#!/bin/bash

BASE=`dirname $0`
cat > $BASE/docs.html <<EOF
<div id="sphinx-docs">
 <ul>
EOF

for i in $BASE/src/* ; do
    DOC=`basename $i`;
    echo "$i > $BASE/docs/`basename $i`";
    if [ ! -d $BASE/docs/$DOC ] ; then
        mkdir -p $BASE/docs/$DOC ;
    fi;
    cp -r $i/build/html/* docs/$DOC;
    git add $BASE/docs/$DOC ;
    cat >> $BASE/docs.html << EOF
    <li><a href="docs/$DOC/">$DOC</a></li>
EOF
done
cat >> $BASE/docs.html <<EOF
  </ul>
</div>
EOF

git commit $BASE  -m "Updates...."
git push $BASE
