.. code-block:: bash

    #!/bin/bash
    #
    PY=/home/system/ve/main/bin/python
    TA=/home/system/ve/main/bin/trac-admin
    BASE=`dirname $0`
    echo $BASE/$1
    $PY $TA $BASE/$1/trac repository resync $2 
