========================
rails コマンド
========================

.. contents::
    :local:

コマンド一覧
===================

.. code-block:: bash

    $ rails --help
    Usage: rails COMMAND [ARGS]
    
    The most common rails commands are:
     generate    Generate new code (short-cut alias: "g")
     console     Start the Rails console (short-cut alias: "c")
     server      Start the Rails server (short-cut alias: "s")
     dbconsole   Start a console for the database specified in config/database.yml
                 (short-cut alias: "db")
     new         Create a new Rails application. "rails new my_app" creates a
                 new application called MyApp in "./my_app"
    
    In addition to those, there are:
     application  Generate the Rails application code
     destroy      Undo code generated with "generate" (short-cut alias: "d")
     benchmarker  See how fast a piece of code runs
     profiler     Get profile information from a piece of code
     plugin       Install a plugin
     runner       Run a piece of code in the application environment (short-cut alias: "r")
    
    All commands can be run with -h (or --help) for more information.

sever 
========

.. list-table:: options

    *   - -p
        - --port=port 
        - サーバを起動するときのポート番号を指定  
        - 3000
    
    *   - -b
        - ---binding=ip    
        - バインドするIPアドレスを指定    
        - 0.0.0.0

    *   - -c
        - --config=file   
        - rackupファイルを指定    
        - 

    *   - -d
        - --daemon    
        - デーモンとしてサーバを起動  
        - 

    *   - -u
        - --debugger  
        - デバックモード  
        - 

    *   - -e
        -  --environment=name  
        - 環境(test/development/production)を指定してサーバを起動 
        - development

    *   - -P
        - --pid=pid   
        - PIDファイルを指定   
        - tmp/pids/server.pid

    *   - -h
        - --help  
        - ヘルプを表示
        -

dbconsole
==============

.. code-block:: bash

    $ rails dbconsole
    SQLite version 3.7.9 2011-11-01 00:52:41
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite> 
