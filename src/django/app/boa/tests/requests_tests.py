# -*- coding: utf-8 -*-
'''
requests  : Requests: HTTP for Humans
----------------------------------------

- http://docs.python-requests.org/en/latest/

'''
from django.test import TestCase

class RequestsTest(TestCase):
    def test_simple(self):
        """

        """
        import requests
        url="http://www.google.com"
        res = requests.get(url)
        print "\n".join([ k + ":" + v for k,v in res.headers.items() ] )
        
    def test_authorizaton_header(self):
        """ Authorizatio ヘッダーを送信

        - http://docs.python-requests.org/en/latest/user/quickstart/#custom-headers 
        """
        #: python manage.py test boa.RequestTest.test_authorizaton_header
        import requests
#        url="http://ec2-54-248-0-242.ap-northeast-1.compute.amazonaws.com/op/Connect/UserInfo/Administrator"
        url="http://ec2-54-248-0-242.ap-northeast-1.compute.amazonaws.com/op/Connect/"
        headers = {'Authorization':'HOGE HOGE',}
        res = requests.get(url,headers=headers)
        print "\n".join([ k + ":" + v for k,v in res.headers.items() ] )
        print res.text
