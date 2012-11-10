# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Favorite(models.Model):
    ''' 嗜好'''
    name    = models.CharField(u'項目',max_length=200,)
    ''' 項目 '''  
    value= models.CharField(u'値',max_length=200,)
    ''' 値 '''  

    class Meta:
        verbose_name =u'嗜好'
        verbose_name_plural =u'嗜好'

class Color(models.Model):
    ''' 色 '''
    name = models.CharField(u'色名',max_length=200,db_index=True,unique=True)
    ''' 色名 '''

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name =u'色'
        verbose_name_plural =u'色'


#for color in ['red','blue','black','yellow','silver','gold']:
#    try:
#        Color(name=color).save()
#    except :
#        pass

class FavoriteColor(models.Model):
    ''' 色の好み　'''
    user = models.ForeignKey(User,verbose_name=u'ユーザ−')
    ''' ユーザ− ''' 
    color =models.ManyToManyField(Color,verbose_name=u'色') 
    ''' 色 '''

    class Meta:
        verbose_name =u'色の好みj'
        verbose_name_plural =u'色の好みj'

