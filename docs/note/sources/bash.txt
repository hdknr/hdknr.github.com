======
bash
======

.. contents:: bash 


Cookbook
===============

sourceされるスクリプトからexitするには？
------------------------------------------

- 単純にexitするとシェルが終了してしまうよ

    .. code-block:: bash

        return 2>&- || exit;

変数
====

.. literalinclude:: _static/bash/args.bash
    :language: bash


$(コマンド)
============

- 実行結果を変数にいれることができる。

::

    (docs)hdknr@sqg:~$ P=$(ps ax|grep bash|awk '{print $1}')
    (docs)hdknr@sqg:~$ echo $P
    2173 2175 2185 2194 2205 2218 2235 2688 2690 2701 2712 2723 2735 2749 12770 12772 12781 12792 12803 12817 12832 15829 15881 17109 17199 17201


配列変数
=========

- () にすると配列変数

- 配列じゃない

::

    (docs)hdknr@sqg:~$ P=$(ps ax|grep bash|awk '{print $1}')
    (docs)hdknr@sqg:~$ echo ${P[0]}
    2173 2175 2185 2194 2205 2218 2235 2688 2690 2701 2712 2723 2735 2749 12770 12772 12781 12792 12803 12817 12832 15829 15881 17109 17218 17224 17226 17227
    (docs)hdknr@sqg:~$ echo ${P[1]}

- 括弧に入れて配列化

::

    (docs)hdknr@sqg:~$ P=($(ps ax|grep bash|awk '{print $1}') )
    (docs)hdknr@sqg:~$ echo ${P[0]}
    2173
    (docs)hdknr@sqg:~$ echo ${P[1]}
    2175

- 配列の全要素( * あるいは @ )

::

    (docs)hdknr@sqg:~$ P=($(ps ax|grep bash|awk '{print $1}'))
    (docs)hdknr@sqg:~$ echo ${P[*]}
    2173 2175 2185 2194 2205 2218 2235 2688 2690 2701 2712 2723 2735 2749 12770 12772 12781 12792 12803 12817 12832 15829 15881 17109 17232 17235 17237

    (docs)hdknr@sqg:~$ echo ${P[@]}
    2173 2175 2185 2194 2205 2218 2235 2688 2690 2701 2712 2723 2735 2749 12770 12772 12781 12792 12803 12817 12832 15829 15881 17109 17232 17235 17237

- 要素数 ( # と * or @ )

::

    (docs)hdknr@sqg:~$ echo ${#P[*]} ${#P[@]}
    27 27

- 最後の値

::

    (docs)hdknr@sqg:~$ echo ${P[ ${#P[@]} - 1]}
    17237


- スライス (スライスした物は配列ではありません )

::

    (docs)hdknr@sqg:~$ echo ${P[@]:4:2}
    2205 2218
    (docs)hdknr@sqg:~$ Q=${P[@]:4:2}
    (docs)hdknr@sqg:~$ echo ${#Q[*]}
    1

    (docs)hdknr@sqg:~$ Q=( ${P[@]:4:2} )
    (docs)hdknr@sqg:~$ echo ${#Q[*]}
    2


- 置換

::

     (docs)hdknr@sqg:~$ echo ${X[@]#*/}
     bin usr/bin usr/local/bin

     (docs)hdknr@sqg:~$ echo ${X[@]##*/}
     bin bin bin

     (docs)hdknr@sqg:~$ echo ${X[@]%*/}
     /bin /usr/bin /usr/local/bin

     (docs)hdknr@sqg:~$ echo ${X[@]%[a-z]*}
     /bi /usr/bi /usr/local/bi

     (docs)hdknr@sqg:~$ echo ${X[@]%%[a-z]*}
     / / /

拡張子の一括変換 ::

    $ for f in *.txt; do echo $f ${f%.txt}.rst ; done

- 要素を抜く


::

    (docs)hdknr@sqg:~$ echo ${#P[*]}
    26
    (docs)hdknr@sqg:~$ unset P[10]
    (docs)hdknr@sqg:~$ echo ${#P[*]}
    25


- declare 内部コマンドでみると、P[10]がないことに注意 !!!!

::

    (docs)hdknr@sqg:~$ declare -p P
    declare -a P='([1]="2175" [2]="2185" [3]="2194" [4]="2205" [5]="2218" 
    [6]="2235" [7]="2688" [8]="2690" [9]="2701" [11]="2723" [12]="2735" [13]="2749" 
    [14]="12770" [15]="12772" [16]="12781" [17]="12792" [18]="12803" [19]="12817" 
    [20]="12832" [21]="15829" [22]="15881" [23]="17109" [24]="17232" [25]="17235" 
    [26]="17237")'


- ちょっと気持ち悪い

::

    (docs)hdknr@sqg:~$ X=(a b c )
    (docs)hdknr@sqg:~$ unset X[1]
    (docs)hdknr@sqg:~$ echo ${#X[*]}
    2

    (docs)hdknr@sqg:~$ declare -p X
    declare -a X='([0]="a" [2]="c")'

    (docs)hdknr@sqg:~$ X[1]='HOGE'
    (docs)hdknr@sqg:~$ declare -p X
    declare -a X='([0]="a" [1]="HOGE" [2]="c")'


seqコマンド
==================

- for でループさせるとき便利よ

::

    (main)hdknr@sqg:~$ for i in $(seq 1 5 ) ; do echo $i; done
    1
    2
    3
    4
    5

for
=====

for コマンドでワイルドカード指定する場合、マッチするファイルがないとワイルドカード指定自体が対象となってしまう


if
====

 - and 

.. code-block:: bash

    if [ "$S" = "1" -a "$SS" = "2" ]
    then
    # ...
    fi

- or

.. code-block:: bash


    if [ "$S" = "1" -o "$SS" = "2" ]
    then
    # ....
    fi


ログインシェル変更
===================

sudo usermod(管理者)
-----------------------------------

::

    system@squeeze02:~$ sudo usermod -s /bin/bash cms
    [sudo] password for system: 
    system@squeeze02:~$ grep cms /etc/passwd
    cms:x:1001:1001::/home/cms:/bin/bash

chsh (自分で変える)
----------------------------

パスワード聞いてきます::

    $ chsh -s /bin/bash

デフォルトの設定ファイル ::

    $ ls -al /etc/skel

    合計 20
    drwxr-xr-x  2 root root 4096 2011-12-31 07:58 .
    drwxr-xr-x 78 root root 4096 2013-08-02 16:23 ..
    -rw-r--r--  1 root root  220 2010-04-10 19:50 .bash_logout
    -rw-r--r--  1 root root 3184 2010-04-10 19:50 .bashrc
    -rw-r--r--  1 root root  675 2010-04-10 19:50 .profile


Link
=======

- 色( http://spiral.world.coocan.jp/tips/computer/lscolor.html )

