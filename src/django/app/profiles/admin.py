# -*- coding: utf-8 -*- 

from django.contrib import admin
from models import *
#
class SimpleProfileAdmin(admin.ModelAdmin):
    list_display=tuple([f.name for f in SimpleProfile._meta.fields])
admin.site.register(SimpleProfile,SimpleProfileAdmin)
#
class PhotoProfileAdmin(admin.ModelAdmin):
    list_display=tuple([f.name for f in PhotoProfile._meta.fields])
admin.site.register(PhotoProfile,PhotoProfileAdmin)
