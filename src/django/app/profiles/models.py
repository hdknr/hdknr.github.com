# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.timezone import now

class Name(models.Model):
    ''' 姓名 '''

    family_name = models.CharField(u'姓',max_length=20)
    ''' 姓 '''
    first_name  = models.CharField(u'名',max_length=20)
    ''' 名 '''
    family_kana = models.CharField(u'カナ姓',max_length=20)
    ''' 姓カナ '''
    first_kana  = models.CharField(u'カナ名',max_length=20)
    ''' 名カナ '''
    
    class Meta:
        verbose_name = u'名前'
        verbose_name_plural = u'名前'
        abstract =True

class Address(models.Model):
    ''' 住所 '''

    zip = models.CharField(u'郵便番号',max_length=7)
    ''' 郵便番号 '''

    prefecture= models.CharField(max_length =50 ,)
    city = models.CharField(max_length =50 ,)
    town = models.CharField(max_length =50 ,)
    street = models.CharField(max_length =70 ,)
    building= models.CharField(max_length =70 ,blank=True,default=None,null=True,)

    class Meta:
        verbose_name = u'住所'
        verbose_name_plural = u'住所'
        abstract =True

class Contact(models.Model):
    ''' 連絡先 '''
    email = models.EmailField() 
    ''' 電子メール '''

    phone = models.CharField(u'電話',max_length=12 )
    ''' 電話 '''
    
    url = models.CharField(u'電話',max_length=12 )
    ''' 電話 '''

    class Meta:
        verbose_name = u'連絡先'
        verbose_name_plural = u'連絡先'
        abstract =True

class AbstractProfile(models.Model):
    user = models.OneToOneField(User,verbose_name=u'システムユーザー',
                                null=True,blank=True,default=None)
    ''' システムユーザー 
        - 通常は OneToOneField , プロファイルを複数管理したいのであれば、ForeignKey にする
    '''

    created_at = models.DateTimeField(u'登録時刻',auto_now_add=True)
    ''' 登録時刻　'''

    updated_at = models.DateTimeField(u'更新時刻',auto_now=True)
    ''' 更新時刻　'''

    class Meta:
        verbose_name = u'個人情報'
        verbose_name_plural = u'個人情報'
        abstract =True

class SimpleProfile(AbstractProfile,Name):
    ''' 名前のみのプロファイル'''
        
    class Meta:
        verbose_name = u'個人情報(簡易)'
        verbose_name_plural = u'個人情報(簡易)'

