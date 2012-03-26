# -*- coding: utf-8 -*-

from django import forms
from models import Favorite,FavoriteColor
from BeautifulSoup import BeautifulSoup as B

class FavoriteForm(forms.ModelForm):
    ''' 嗜好フォーム'''

    value= forms.MultipleChoiceField(
            choices=(
                (u'blue',u'blue'),
                (u'red',u'red'),
                (u'yellow',u'yellow'),
                (u'pink',u'pink'),
                (u'black',u'black'),
            )
        )
    ''' 値 '''  
    class Meta:
        model = Favorite

class FavoriteTypedForm(forms.ModelForm):
    ''' 嗜好フォーム'''
    def coerce(choice):
        print "your chice is ",choice 

    value= forms.TypedMultipleChoiceField(
            coerce=coerce,
            choices=(
                (u'blue',u'blue'),
                (u'red',u'red'),
                (u'yellow',u'yellow'),
                (u'pink',u'pink'),
                (u'black',u'black'),
            ),
        )
    ''' 値 '''  
    class Meta:
        model = Favorite

class FavoriteColorForm(forms.ModelForm):
    ''' 色の嗜好フォーム'''
    class Meta:
        model = FavoriteColor
