#!/bin/bash

cat > docs.html <<EOF
<div id="sphinx-docs">
 <ul>
EOF

for i in src/* ; do
    DOC=`basename $i`;
    echo "$i > docs/`basename $i`";
    if [ ! -d docs/$DOC ] ; then
        mkdir -p docs/$DOC ;
    fi;
    cp -r $i/build/html/* docs/$DOC;
    git add docs/$DOC ;
    cat >> docs.html << EOF
    <li><a href="docs/$DOC/">$DOC</a></li>
EOF
done
cat >> docs.html <<EOF
  </ul>
</div>
EOF

#git commit -a -m "Updates...."
#git push
