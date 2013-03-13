=======
置換
=======

.. contents::
    :local:

Sphinx
============================

term
--------------------

ソース ::

    "Access Token",
    "Refresh Token",

コマンド::
    

    :'<,'>s/"\(.*\)"/":term:\`\1`"/g
    

結果::

    ":term:`Access Token`",
    ":term:`Refresh Token`",

rfc
----

::

    :%s/RFC \(.*\),/:rfc:\`\1`,/g

