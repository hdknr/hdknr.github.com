# -*- coding: utf-8 -*-

import sys
if sys.version_info < (2,7):
    import unittest2 as unittest
else:
    import unittest

class HttpTest(unittest.TestCase):
    def test_http_get_detail(self):
        '''
        nosetests -s  tests.py:HttpTest.test_http_get_detail
        '''
        import urllib2
        import httplib
        url = "http://www.google.com"
        req = urllib2.Request(url)
        res = urllib2.urlopen(req )
        print res
        print "getcode=",res.getcode(),type(res.getcode())
        print "code=",res.code,type(res.code)
        print "geturl=",res.geturl(),type(res.geturl())
        print "url=",res.url,type(res.url)
        print "headers======\n",type(res.headers)                  # print dir(res.headers)
        print res.headers['Content-Type']
        print "- maintype",res.headers.maintype
        print "- subtype",res.headers.subtype
        print "- getencoding",res.headers.getencoding()
        print "- gettype",res.headers.gettype()
        print "- status",res.headers.status
        print "- dict",res.headers.dict
        print dir(res.headers)
#        print "- mimetype",res.headers.mimetype
        self.assertEqual(type(res.headers.headers) ,list ) #:LIST,res.headers.headers
        
        for k,v in res.headers.items():
            print "-",k,"=",v
        print "info=\n",type(res.info()),isinstance(res.info(),httplib.HTTPMessage)
        print "msg=\n",res.msg,type(res.msg) 
        #print res.read()

    def test_http_get_detail_jsonpickle(self):
        '''  $ pip install jsonpickle
        '''
        import jsonpickle
        import urllib2
        import httplib
        url = "http://www.google.com"
        req = urllib2.Request(url)
        res = urllib2.urlopen(req )
        pickled = jsonpickle.encode(res)
        print pickled   

    def test_res_header_isnot_json_serializable(self):
        '''  $ pip install jsonpickle

        nosetests -s  tests.py:HttpTest.test_res_header_isnot_json_serializable
        '''
        import json
        import urllib2
        import httplib
        url = "http://www.google.com"
        req = urllib2.Request(url)
        res = urllib2.urlopen(req )

        with self.assertRaises(TypeError  ):
            text = json.dumps(res.headers) 
        
        print json.dumps( {}.update(res.headers) )

    def test_invalid_host(self):
        '''
        nosetests -s  tests.py:HttpTest.test_invalid_host
        '''
        import json
        import urllib2
        url = "http://www.google.comm"
        req = urllib2.Request(url)

        try:
            res = urllib2.urlopen(req )
        except urllib2.URLError,e:
            print "urllib2.URLError is raised", type(e),type( e.reason),
            self.assertEqual(e.reason.errno,-2)        # <urlopen error [Errno -2] Name or service not known>

