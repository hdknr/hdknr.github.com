#!/bin/bash
MODELS="accounts openid oauth"
echo  ${MODELS}
RST=source/accounts_models.rst
for M in ${MODELS} ; do

    if [ ! -d source/${M} ]; then
        mkdir -p source/${M};
    fi;

    if [ ! -f $RST ] ; then
        echo "================="  >  $RST;
        echo "${M} ER" >> $RST;
        echo "================="  >> $RST;
        echo "" >> $RST;
        echo ".. include:: ${M}/models.dot " >>  $RST;
    fi

    echo ".. digraph:: ${M}" > source/${M}/models.dot ;
    echo "" >> source/${M}/models.dot ;
    python ../app/manage.py graph_models ${M}| grep "^ " >> source/${M}/models.dot;

done

