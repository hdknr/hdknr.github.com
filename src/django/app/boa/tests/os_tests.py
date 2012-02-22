# -*- coding: utf-8 -*-

import sys 
if sys.version_info < (2,7):
    import unittest2 as unittest
else:
    import unittest

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

        with self.assertRaises(OSError) as ex:
            #: 既存のディレクトリを再度作成しようとするとエラー
            os.makedirs(dirname) 
        self.assertEqual(ex.exception[0],17 )
#        for e in ex.exception:
#            print type(e),e
            
        self.assertEqual(os.path.isdir(dirname),True)
        os.removedirs( dirname )
        self.assertEqual(os.path.isdir(dirname),False)
