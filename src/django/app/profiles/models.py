# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.timezone import now

#from django.db.models.signals import post_save
from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete)

import os

class Name(models.Model):
    ''' 姓名 '''

    family_name = models.CharField(u'姓',max_length=20,default='')
    ''' 姓 '''
    first_name  = models.CharField(u'名',max_length=20,default='')
    ''' 名 '''
    family_kana = models.CharField(u'カナ姓',max_length=20,default='')
    ''' 姓カナ '''
    first_kana  = models.CharField(u'カナ名',max_length=20,default='')
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

class UserSignalMixIn:
    ''' '''
    @classmethod
    def connect(cls, *signals):
        """ User クラスがの操作のシグナル処理　"""
        for signal in signals:        
            sig_handler = {
                pre_save: cls.on_pre_save,
                post_save: cls.on_post_save,
                pre_delete: cls.on_pre_delete,
                post_delete: cls.on_post_delete,
                }[signal]
            signal.connect(sig_handler, sender=User)

    @classmethod
    def on_pre_save(cls,sender, **kwargs):
        pass

    @classmethod
    def on_post_save(cls,sender, **kwargs):
        user, created = kwargs["instance"], kwargs["created"]
        if created:
            cls.objects.create(user=user)

    @classmethod
    def on_pre_delete(cls,sender, **kwargs):
        pass

    @classmethod
    def on_post_delete(cls,sender, **kwargs):
        pass


class SimpleProfile(AbstractProfile,Name,UserSignalMixIn):
    ''' 名前のみのプロファイル'''
        
    class Meta:
        verbose_name = u'個人情報(簡易)'
        verbose_name_plural = u'個人情報(簡易)'

class PhotoProfile( AbstractProfile ):

    def photo_filename(instance,filename):
        """ アップロードファイルには拡張子が入っている事 
            (view+formで確認)
            - os.path.splittext() は ドット付きの拡張子を返す
        """
        return  "profiles/image.%d%s" % ( instance.id  , os.path.splitext(filename)[1] )

    photo = models.ImageField("Photo", upload_to=photo_filename,
                                null=True,default=None,blank=True) 
    
    class Meta:
        verbose_name = u'個人情報(写真)'
        verbose_name_plural = u'個人情報(写真)'

### receiverデコレータを使う：保存後シグナルを受け取ってハンドラをディスパッチさせる 
#from django.dispatch import receiver
#
#@receiver(post_save, sender=User)
#def user_post_save(sender, **kwargs):
#    user, created = kwargs["instance"], kwargs["created"]
#    if created:
#        SimpleProfile.objects.create(user=user)


#: UserSignalMixIn を使う
SimpleProfile.connect(post_save,)


