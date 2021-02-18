from django.contrib import admin
from .models import *

admin.site.site_header = "Taffy Admin."
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','age','rasi','bloodtype','naksus')
    list_display_links = ('id', 'user')
    list_filter = ('user','testes','gender' ,)
    list_per_page = 20

admin.site.register(Profile, ProfileAdmin)
admin.site.register(BloodType)
admin.site.register(DaysOfWeek)
admin.site.register(NakSus)
admin.site.register(RaSi)
admin.site.register(Personality)
admin.site.register(Gender)
admin.site.register(Testes)
admin.site.register(Handler)
admin.site.register(Goldmember)
admin.site.register(Conversation)
# @admin.register(settings.AUTH_USER_MODEL,Member)
