CLI
=====

.. contents::
    :local:


REPL( Read-eval-print loop)
----------------------------

* -a オプション*

::
    --interactive
    -a             
    
        Run PHP interactively. 
        This lets you enter snippets of PHP code that directly get executed. 
        When readline support is enabled  you  can  edit  the lines 
        and also have history support.

.. code-block:: php

    (docs)Peeko:php hide$ php -a

    Interactive shell
    php > ini_set( "date.timezone", "Asia/Tokyo");
    php > echo date( "Y/m/d (D) H:i:s", time() ) ;
    2013/09/15 (Sun) 05:44:26
