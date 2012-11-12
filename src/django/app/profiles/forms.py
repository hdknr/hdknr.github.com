# -*- coding: utf-8 -*- from django import forms

from django import forms
from django.conf import settings
from django.core.files import File

from models import PhotoProfile

import os
import uuid

MEDIA= lambda f : os.path.join( settings.MEDIA_ROOT,f )
PREVIEW = lambda f : "preview/" + f
try:
    os.makedirs( MEDIA('preview') )
except Exception,e:
    pass

class PhotoProfileForm(forms.ModelForm):

    photo_preview = forms.CharField(widget= forms.HiddenInput ,required=False,)

    def __init__(self,*args,**kwargs):
        super(PhotoProfileForm,self).__init__(*args,**kwargs)

    def save(self,*args,**kwargs):
        try: 
            #:変更があったら以前のファイルを削除
            for field_name,field in self.fields.items():
                if isinstance(field, forms.fields.FileField) and getattr(self.instance,field_name) and \
                    ( os.path.isfile( MEDIA(self.cleaned_data.get( field_name + "_preview") ) ) or
                      self.cleaned_data.get( field_name + "_preview")   == "delete"
                    ) : 
                    getattr(self.instance,field_name).delete()

            #:更新
            super(PhotoProfileForm,self).save( )
    
            #:プレビューファイルの処理
            for field_name,field in self.fields.items():
                if isinstance(field, forms.fields.FileField) and self.cleaned_data[field_name + "_preview"] not in ['','delete']:
                    preview_file = MEDIA( self.cleaned_data[field_name + "_preview"] )
                    #:コピーして保存
                    getattr(self.instance,field_name).save( preview_file,
                            File(open(preview_file) )
                        ) 
                    os.remove(preview_file )    #:プレビューを削除

        except Exception,e:
            pass
                    
    def to_preview(self):
        ''' フォームのアイテムを全てhiddeに変更する 
        '''
        for k,f in self.fields.items():
            if str(type(f)).find('Multi') >0: 
                f.widget = forms.MultipleHiddenInput() 

            elif isinstance(f, forms.fields.FileField):
                if self.cleaned_data[k] == False :
                    #:削除
                    self.fields[k + "_preview"].widget = forms.HiddenInput(
                                                attrs={'value':'delete',}) 
                elif self.cleaned_data[k] and k  in self.changed_data: 
                    #:アップロードがあったら 
                    file_data = getattr(self.instance,k,None ) 
                    if file_data != None and file_data.name :
                        ext =os.path.splitext(file_data.name )[1]  
                        file_data.name= self.cleaned_data.get('photo_preview' ) if self.cleaned_data.get('photo_preview' ) != "" \
                                        else PREVIEW(uuid.uuid1().hex +  ext)
                        #: ファイルを一時保存
                        open( MEDIA(file_data.name),"w").write( file_data.file.read() )
                    self.fields[k + "_preview"].widget = forms.HiddenInput(
                                                    attrs={'value':file_data.name,}) 
                    self.fields[k + "_preview"].initial=file_data.name
                else:
                    #: ファイルの指定が無い場合
                    if self.cleaned_data.get('photo_preview' ) != "":
                        os.remove( MEDIA( self.cleaned_data.get('photo_preview' )) )
                    self.fields[k + "_preview"].widget = forms.HiddenInput( attrs={'value':'',}) 
                    self.fields[k + "_preview"].initial= ''

                #: FileFiledをHidden化
                f.widget = forms.HiddenInput()

            elif isinstance(f.widget, forms.HiddenInput ) == False:
                f.widget = forms.HiddenInput() 
        
    
    class Meta:
        model= PhotoProfile
        exclude = ['user',]
