"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.contrib.auth.models import User
from models import  SimpleProfile

class SimpleTest(TestCase):
    def test_postcreated(self):
        """
        """

        total = SimpleProfile.objects.count()

        username="hoge"
        params = {'email': 'hoge@hoge.com', 'password': 'hogewd', } 
        u = User.objects.create_user( username, **params )
        print u , "is created"
        self.assertEquals( SimpleProfile.objects.count(),total + 1)
        
        self.assertEquals( u.email, SimpleProfile.objects.get(user__username = username).user.email )
        u.delete()

        self.assertEquals( SimpleProfile.objects.count(),total)
