===========
Github
===========

GitHub Pages
=============

Underscore
-----------

Github Pages( http://pages.github.com/ ) では、アンダースコア付きのファイルのパブリッシュが出来ない。
ので、Sphinxでビルドする _static ディレクトリを static などにリネームする必要があります。

sphinx-to-github (https://github.com/michaeljones/sphinx-to-github) で対応できます。

:: 

    $ pip install -e git+https://github.com/michaeljones/sphinx-to-github.git#egg=sphinxtogithub


conf.py:  

.. code-block:: python

    extensions.append('sphinxtogithub')  #:GITHUB


