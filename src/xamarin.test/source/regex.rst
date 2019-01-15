==============
正規表現
==============

.. contents::
    :local:


パターン
==========

Named Capture
----------------

- Python と同じ

::

    (?P<name>.+)


Optional Group Capture
------------------------
  
::

    (?:表現)?



preg_match
===========

- URLのマッチング

.. code-block:: php


    $pattern='/^(?:(?P<scheme>https*))?'.
             '(?:[:\/]+)?'.
             '(?P<host>[^\?#\/:]+)'.
             '(?::(?P<port>\d+))?'.
             '(?P<path>[^#\?]*)'.
             '(?:\?(?P<query>[^#]+))?'.
             '(?:#(?P<fragment>.*))?/';
 
    $matches = Array();
    $url = "http://hoge.com:9000/path#frag=xxx";
    if( preg_match( $pattern, $url ,$matches)) {
        echo( var_dump( $matches ) );
    } 

    
