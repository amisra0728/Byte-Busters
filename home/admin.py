from django.contrib import admin
from home.models import *
# Register your models here.

# class ProfileTypeAdmin(admin.ModelAdmin):
admin.site.register(ProfileType)
# admin.site.register(User)
# admin.site.register(Unit)
# admin.site.register(Requirements)
# admin.site.register(SiteVisit)
admin.site.register(Flat)
admin.site.register(Flatmate)