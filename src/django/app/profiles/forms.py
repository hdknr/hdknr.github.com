# -*- coding: utf-8 -*- from django import forms
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from models import Profile

class ProfileEditForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(ProfileEditForm,self).__init__(*args,**kwargs)
        self.fields['building'].required=False
    
    def to_preview(self):
        ''' フォームのアイテムを全てhiddeに変更する '''
        for k,f in self.fields.items():
            if str(type(f)).find('Multi') >0:
                f.widget = forms.MultipleHiddenInput() 
            else:
                f.widget = forms.HiddenInput() 

    class Meta:
        model= Profile
        exclude = ['user','session_key', ]
    
