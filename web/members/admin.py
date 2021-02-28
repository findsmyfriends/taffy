from django.contrib import admin
from .models import *

admin.site.site_header = "Taffy Admin."
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','age','rasi','bloodtype','naksus','gender','testes')
    list_display_links = ('id', 'user')
    list_filter = ('user','testes','gender',)
    list_per_page = 20
class PersonalityAdmin(admin.ModelAdmin):
    list_display = ('id','personality')
    list_display_links = ('id', 'personality')
    list_per_page = 20
admin.site.register(Profile, ProfileAdmin)
admin.site.register(BloodType)
admin.site.register(DaysOfWeek)
admin.site.register(NakSus)
admin.site.register(RaSi)
admin.site.register(Personality,PersonalityAdmin)
admin.site.register(Gender)
admin.site.register(Testes)
admin.site.register(Handler)
admin.site.register(Goldmember)
admin.site.register(Match)
admin.site.register(Message)
# admin.site.register(Conversation)
# @admin.register(settings.AUTH_USER_MODEL,Member)
