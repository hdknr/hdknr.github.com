# -*- coding: utf-8 -*-
'''
os: Python OS package
----------------------------------------


'''
from django.test import TestCase

class OsTest(TestCase):
    def test_dir(self):
        """
        python manage.py test boa.OsTest.test_dir
        """
        import os
       
        dirname = ".sandbox/hoge" 
        if os.path.isdir(dirname) == False:
            os.makedirs(dirname) 
        self.assertEqual(os.path.isdir(dirname),True)
        os.removedirs( dirname )
        self.assertEqual(os.path.isdir(dirname),False)
