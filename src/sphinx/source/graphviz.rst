============
Graphviz
============

.. contents:: sphinx.ext.graphviz

ライブラリ
===========

graphviz
---------

dotコマンド

::

    $ sudo aptitude install graphviz

graphviz-dev
--------------

::

    $ sudo aptitude install graphviz-dev
    

pygraphviz
--------------

::

    $ pip install pygraphviz

Extension 設定
==============================

conf.py

.. code-block:: python

    extensions.append('sphinx.ext.graphviz')


