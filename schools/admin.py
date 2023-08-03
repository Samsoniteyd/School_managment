from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Registration)

class courseAdmin(admin.ModelAdmin):
    list_display= ['title', 'name']
admin.site.register(course, courseAdmin)  