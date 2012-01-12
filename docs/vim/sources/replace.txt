=======
置換
=======


Sphinx のクロスリファレンス
============================

ソース ::

    "Access Token",
    "Refresh Token",

コマンド::
    

    :'<,'>s/"\(.*\)"/":term:\`\1`":
    

結果::

    ":term:`Access Token`":,
    ":term:`Refresh Token`":,
