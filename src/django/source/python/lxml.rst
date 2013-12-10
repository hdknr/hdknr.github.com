=========
lxml
=========

.. contents::
    :local:

Install
========

.. code-block:: bash

    $ pip install lxml


How To
=========

XMLファイル読み込み
---------------------

.. code-block:: python

    import urllib2
    from lxml import etree

    xml = etree.fromstring(
        urllib2.urlopen('http://yousite.com/rss').read() )

.. code-block:: python

    >>> from lxml import etree
    >>> root = etree.parse( open("Components.wxs"), parser=etree.XMLParser())

ドキュメント情報
------------------------


.. code-block:: python
    
    >>> type(root)
    <type 'lxml.etree._ElementTree'>
   
    >>> root.docinfo.root_name
    'Wix' 


    
