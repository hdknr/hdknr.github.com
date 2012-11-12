# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django import template
from django.conf import settings
from models import *
from forms import *

def default(request):
    return render_to_response( 'profiles/default.html',
        { } ,
        context_instance=template.RequestContext(request),)

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class PhotoProfileView(FormView):
    template_name = "profiles/photo/edit.html"
    form_class = PhotoProfileForm

    def dispatch(self, request, *args, **kwargs):
        #:
        try:
            #: call form_valid, form_invalid
            res =  super(PhotoProfileView,self).dispatch(request,*args,**kwargs)
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
            vals =  self.get_form_kwargs()   #:POST & FILES
            if self.kwargs.get('id','None'):
                vals['instance'] = form_class._meta.model.objects.get(id=self.kwargs['id'])
            ret = form_class( ** vals )
            return ret
        except Exception,e:
            #:TODO エラー処理
            raise e

        return form_class()          #:TODO: should be error?      

    def get_context_data(self, **kwargs):
        ''' コンテキストデータ '''
        ret = super(PhotoProfileView,self).get_context_data(**kwargs)
        #: 追加はここで
        return ret
    
    def form_valid(self, form):
        ''' ''' 
        action = self.request.POST.get('action',u'edit') 

        { 
            "save": lambda : form.save(),
            "edit": lambda : True,
            "preview": lambda : form.to_preview(),
        }[action](); 

        self.template_name = "profiles/photo/%s.html" % action
                
        return self.render_to_response(self.get_context_data(
                        form = form
                    ))
        
    def form_invalid(self, form):
        return super(PhotoProfileView ,self).form_invalid(form)
