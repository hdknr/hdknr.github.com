============
Markdown
============

.. content::
    :local:

pandocで変換
=============

OSX
------

::

    $ brew install pandoc
    ==> Installing pandoc dependency: gmp
    ==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/gmp-6.0.0a.mavericks.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring gmp-6.0.0a.mavericks.bottle.tar.gz
    🍺  /usr/local/Cellar/gmp/6.0.0a: 15 files, 3.2M
    ==> Installing pandoc
    ==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/pandoc-1.13.1.mavericks.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring pandoc-1.13.1.mavericks.bottle.tar.gz


変換
---------

::

    $ cat sample.md 

    # Convert Markdown to reStructuredText
    
    ## pandoc
    
    ~~~
    $ bew install pandoc
    ~~~
    
    ## pypandoc
    
    ~~~
    $ pip isnstall pypandoc
    ~~~
    

::

    $ pandoc -f markdown -t rst sample.md 

    Convert Markdown to reStructuredText
    ====================================
    
    pandoc
    ------
    
    ::
    
        $ bew install pandoc
    
    pypandoc
    --------
    
    ::
    
        $ pip isnstall pypandoc
    

