==========
Mercurial
==========

Cheat
======

- http://troter.jp/mercurial-cheatsheet/

未登録ファイルを全て追加
----------------------------------------

オプション、引数無しで hg add 

:: 

    (docs)hdknr@sqg:~/ve/docs/tmp/bitinit$ hg status
    R requirments.txt
    ? AUTHORS
    ? INSTALL
    ? LICENSE
    ? MANIFEST.in
    ? NOTICE
    ? README
    ? conf.yml
    ? requirements.txt
    ? setup.cfg
    ? setup.py

    (docs)hdknr@sqg:~/ve/docs/tmp/bitinit$ hg add
    AUTHORS を追加登録中
    INSTALL を追加登録中
    LICENSE を追加登録中
    MANIFEST.in を追加登録中
    NOTICE を追加登録中
    README を追加登録中
    conf.yml を追加登録中
    requirements.txt を追加登録中
    setup.cfg を追加登録中
    setup.py を追加登録中

Flow
=====

- hgflow : https://bitbucket.org/yujiewu/hgflow/wiki/Home


Bitbucket
==========

- API : http://confluence.atlassian.com/display/BITBUCKET/Repositories
   



Git/Mercurial
======================


.. list-table::
    :header-rows: 1

    * - タスク
      - :doc:`Git <git>`
      - Mercural

    * - 最初の取得
      - git clonse {{url}}
      - hg clone {{url}}

    * - 最新の取得(のみ)(a)
      - git fetch
      - hg pull

    * - 取得したもので更新(b)
      - git merge origin/master
      - hg update [#]_

    * - 最新を取得して更新(a+b)
      - git pull
      - hg pull -u

.. [#] hg up, hg checkout, hg co 等でも良い
