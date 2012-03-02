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
        
