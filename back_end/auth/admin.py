from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Profile
# Register your models here.
  




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    list_filter = ('user', )
    list_per_page = 20

admin.site.register(Profile, ProfileAdmin)