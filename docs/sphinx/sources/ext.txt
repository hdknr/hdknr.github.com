===================
Extensions
===================

:mod:`sphinx.ext.intersphinx <sphinx:sphinx.ext.intersphinx>` 
===============================================================

他のSphinxプロジェクトのobject.inv ファイルを参照して、簡単なマークアップを指定してリンクを生成する事ができます。

拡張を宣言します (conf.py):

.. code-block:: python

    extensions = [ ...
                'sphinx.ext.intersphinx', 
                    ... 
                ]

他のSphinxサイトを参照します(PythonとSphinxを参照しています) :

.. code-block:: python

    intersphinx_mapping = {'http://docs.python.org/': None,
                        'sphinx': ('http://sphinx.pocoo.org/',None),
                      }

Sphinxの sphinx.ext.intersphinx の mod を参照する(セクションヘッダーのリンク)には以下のようにします. :

.. code-block:: rst

    :mod:`sphinx.ext.intersphinx <sphinx:sphinx.ext.intersphinx>` 

.. note::
    これだとうまく行っていないような気がする::
        
        :mod:`<sphinx:sphinx.ext.intersphinx>` 
            
また、 Sphinxの用語":term:`sphinx:builder`" にリンクするには以下のようにします :

.. code-block:: rst

    :term:`sphinx:builder`


