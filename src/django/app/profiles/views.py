# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django import template
from django.conf import settings
from models import *
from forms import *

def default(request):
    ''' default page (test)'''
    return render_to_response( 'profiles/default.html',
        { } ,
        context_instance=template.RequestContext(request),)

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class ProfileEditView(FormView):
    template_name = "profiles/edit.html"
    form_class = ProfileEditForm

    def dispatch(self, request, *args, **kwargs):
        #:
        try:
            #: call form_valid, form_invalid
            res =  super(ProfileEditView,self).dispatch(request,*args,**kwargs)
            #: force not redirect  
            return res
        except Exception,e:
            return self.render_to_response(self.get_context_data(
                        form=self.get_form(self.form_class)
                    ))

    def get_form(self, form_class): 
        ''' API: return するフォームは 'form' というコンテキストで参照できます。
        '''
        try: 
            ret = form_class( data = self.request.POST)
            return ret
        except Exception,e:
            #:TODO エラー処理
            print ">>>>>",e

        return form_class()          #:TODO: should be error?      

    def get_context_data(self, **kwargs):
        ''' コンテキストデータ '''
        ret = super(ProfileEditView,self).get_context_data(**kwargs)
        #: 追加はここで
        return ret
    
    def form_valid(self, form):
        ''' ''' 
        action = self.request.POST.get('action',[u'edit']) 
        try:
            if 'save' in action:
                form.instance.session_key = self.request.session.session_key 
                form.save()
                self.template_name = "profiles/saved.html"
            elif 'edit' in action:
                self.template_name = "profiles/edit.html"
            else:
                form.to_preview()
                self.template_name = "profiles/preview.html"
        except Exception,e:
            print e
                
        return self.render_to_response(self.get_context_data(
                        form = form
                    ))
        
    def form_invalid(self, form):
        return super(ProfileEditView ,self).form_invalid(form)
