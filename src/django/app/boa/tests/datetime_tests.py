# -*- coding: utf-8 -*-

import sys 
if sys.version_info < (2,7):
    import unittest2 as unittest
else:
    import unittest

'''
datetime : Python datetime package
----------------------------------------


'''
from django.test import TestCase


class DateTimeTest(TestCase):
    def test_strptime(self):
        """
        python manage.py test boa.OsTest.test_strptime
        """
        from datetime import datetime
        
        def datetime_from_str(dt= None,fmt='%Y-%m-%d %H:%M:%S'):
            try:
                return datetime.strptime(dt,fmt)
            except:
                return datetime.now()

        dt= datetime_from_str()
        self.assertEqual(type(dt),datetime)

        src='2012-02-26 06:42:32'
        self.assertEqual(datetime_from_str(src).strftime('%Y-%m-%d %H:%M:%S'),src)

        src='2011-02-26'
        dt=datetime_from_str(src,fmt='%Y-%m-%d')
        self.assertEqual(dt.strftime('%Y-%m-%d %H:%M:%S'),src+dt.strftime(" %H:%M:%S" ))
