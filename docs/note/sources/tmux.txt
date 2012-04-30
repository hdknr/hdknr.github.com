======
tmux
======

.. contents:: tmux

凡例
=====

.. list-table:: 

    *   - ec 
        - Escape Character とします。デフォルト b 

    *   - ec-c
        - Escape Characterに続いて c を入力するとします。

Pane
====

現在のウィンドウを別のウィンドウのペイントして追加::


    :join-pane -t 3 

デフォルトで上下分割なので、左右分割にするには::

    :select-layout even-horizontal 
    

ペイン間を移動します ::

    ec-o

現在のウィンドウのペインを解除します。::

    ec-!

別のウインドウを現在のウィンドウのペインに追加::

    :join-pane -s 5

