from django.contrib import admin

from e_mypolice.forms import firForm
from .models  import login_data,contactus,fir,missingperson,stolenproperty
# Register your models here.

class loginadmin(admin.ModelAdmin):
    list_display=['fullname']

class contactAdmin(admin.ModelAdmin):
    list_display=['name']

class firAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname']

class missingpAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname']

class stolenAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname']

admin.site.register(login_data,loginadmin)

admin.site.register(contactus,contactAdmin)

admin.site.register(fir,firAdmin)

admin.site.register(missingperson,missingpAdmin)

admin.site.register(stolenproperty,stolenAdmin)