::

    Include /home/system/trac.lafoglia.jp/conf/macro.def

    # Virtual Host
    Use VHost trac.lafoglia.jp /home/system 443
    
    # WSGI
    Usr WSGI /home/system/ve/main lafoglia apps 
    Usr WSGI /home/system/ve/main lafoglia services

    # Virtual Directory for each project
    Use Trac trac.lafoglia.jp /home/system lafoglia apps
    Use Trac trac.lafoglia.jp /home/system lafoglia servcies
