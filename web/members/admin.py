from django.contrib import admin
from .models import Profile

admin.site.site_header = "Taffy Admin."
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','age')
    list_display_links = ('id', 'user')
    list_filter = ('user', )
    list_per_page = 20

admin.site.register(Profile, ProfileAdmin)

# @admin.register(settings.AUTH_USER_MODEL,Member)
