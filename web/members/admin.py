
from django.contrib import admin
from django.db.models.base import ModelBase
from .models import *


admin.site.site_header = "Taffy Admin."
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','first_name','last_name','email')
    list_display_links = ('id', 'username')
    list_per_page = 20
admin.site.register(Member, MemberAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','age','daysofweek','rasi','bloodtype','naksus','gender','testes')
    list_display_links = ('id', 'user')
    list_filter = ('user','testes','gender',)
    list_per_page = 20
admin.site.register(Profile, ProfileAdmin)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'reqUser','ratedUser','ratingPoint')
    list_display_links = ('id', 'ratedUser')
    list_filter = ('reqUser',)
    list_per_page = 20
admin.site.register(Rating,RatingAdmin)
admin.site.register(BloodType)
admin.site.register(DaysOfWeek)
admin.site.register(NakSus)
admin.site.register(RaSi)
admin.site.register(Handler)
admin.site.register(Match)
admin.site.register(Message)

# admin.site.register(ScoreOfRaSi) 
# admin.site.register(ScoreOfNakSus)
# admin.site.register(ScoreOfDaysOfWeek)
# admin.site.register(ScoreOfBloodType)
# admin.site.register(Personality,PersonalityAdmin)
# admin.site.register(Gender)
# admin.site.register(Testes)
# admin.site.register(Goldmember)
# admin.site.register(Conversation)
# @admin.register(settings.AUTH_USER_MODEL,Member)
