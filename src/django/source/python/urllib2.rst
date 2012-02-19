.. _python.urllib2.basicauth:

基本認証のAPIコールでJSONを送る
------------------------------------------

.. code-block:: python

    import json
    import urllib2
    def send_json(endpoint,jsonstring):
        ''' JSON を ポストします　
        '''
    
        #: For Basic Authentication    
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()    
        passman.add_password(None, endpoint, API_USER['username'], API_USER['password'])    
        opener = urllib2.build_opener(authhandler)    
        urllib2.install_opener( 
                urllib2.build_opener( 
                    urllib2.HTTPBasicAuthHandler(passman)    
                ))

        #: Request    
        req = urllib2.Request(endpoint,  jsonstring, {'Content-Type': 'application/json',
            'Content-Length': len(jsonstring), 'charset':'utf-8'})    

        #: HTTP    
        f = urllib2.urlopen(req)    
        response = f.read()    
        f.close()
        returnn response
