#
'''
$ pip install Werkzeug
'''
import os
import mimetypes
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    print "UA=",request.user_agent
    p = os.path.join(      
            os.path.dirname(os.path.abspath(__file__)) , request.path[1:] 
        ) +(  'index.html' if request.path[-1:] == '/' else '' )
    
    try:
        response = Response(open(p).read(), mimetype=mimetypes.guess_type(os.path.basename(p))[0] )
        return response(environ, start_response)
    except Exception,e:
        return Response( str(type(e)) + " " + str(e ) + " for " + p , mimetype='text/plain', )(environ,start_response )

from werkzeug import run_simple
run_simple('0.0.0.0', 8800, application)

