#-*- coding: utf-8 -*-

# - configure logging

def config(LOGGING):
    ''' ログ設定をします 

        - settigns.py から 呼びます

    >>> import applogs
    >>> applogs.config(LOGGING)
    '''
    #: custom formatter
    if not LOGGING.has_key('formatters') : 
        LOGGING['formatters']={} 
        
    LOGGING['formatters']['parsefriendly'] = { 
        'format': '[%(levelname)s] %(asctime)s - M:%(module)s, P:%(process)d, T:%(thread)d, MSG:%(message)s',
        'datefmt': '%d/%b/%Y:%H:%M:%S %z',
    }

    #  customer handler (console)
    LOGGING['handlers']['console'] = { 
        'level':    'DEBUG',
        'class':    'logging.StreamHandler',
    }

    #  customer handler (file)
    LOGGING['handlers']['file'] = { 
        'level':    'DEBUG',
        'class':    'logging.handlers.TimedRotatingFileHandler', 
        'formatter':'parsefriendly',
        'when':     'midnight',
        'filename': 'app.log',
    }

    #  customer logger (app)
    LOGGING['loggers']['app'] = { 
        'handlers': ['console'],
        'level':    'DEBUG', 
        'propagete':    True,
    }

    #  customer logger (sys)
    LOGGING['loggers']['sys'] = { 
        'handlers': ['file'],
        'level':    'DEBUG', 
        'propagete':    True,
    }

def get_logger():
    ''' 環境変数 APP_LOGGER から logger を読み取って loggingを返します。
    '''
    # - logging api 
    import logging,os
    return  logging.getLogger(os.environ.get('APP_LOGGER','app'))

def sample_request_handler(request):
    '''  サンプルリクエストハンドラ
    ''' 
    
    logger = get_logger() 
 
    # - views  
    from django import template
    from django.http import HttpResponse

    #: ログを書きます。
    logger.debug( "\n".join( [ "%s=%s" % ( k,v )  for k,v in request.META.items() ]))
    
    return HttpResponse(
        template.Template("""
        <html><head><title>Log sample</title></head> <body> <h1> Log Sample</h1>
        Your Logger : {{ logger }}
        name = {{logger.name}} <br/>
        level = {{logger.level }} <br/>
        propagate = {{logger.propagate}} <br/>
        parent = {{logger.parent}} <br/>
        root = {{logger.root}} <br/>
        """
        ).render( template.RequestContext(request,{'logger':logger}) )
    )
