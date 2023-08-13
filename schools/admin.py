from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Registration)

class courseAdmin(admin.ModelAdmin):
    list_display= ['title', 'name']
admin.site.register(course, courseAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display= ['image', 'title']
admin.site.register(slider, sliderAdmin)

class testmonialAdmin(admin.ModelAdmin):
    list_display= ['image', 'name']
admin.site.register(testmonial, testmonialAdmin)
