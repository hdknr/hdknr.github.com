.. code-block:: python

    import os,sys
    #
    current = os.path.dirname(os.path.abspath(__file__)) 
    #
    sys.stdout = sys.stderr
    os.environ['TRAC_ENV'] = "%s/trac" % current
    os.environ['PYTHON_EGG_CACHE'] = "%s/cache" % current
    #
    from trac.web.main import dispatch_request
    application = dispatch_request
