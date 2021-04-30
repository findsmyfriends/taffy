from django.contrib import admin
from .models import *
from datetime import date
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

admin.site.site_header = "Taffy Admin."
admin.site.unregister(auth.models.Group)
# admin.site.unregister(Group)
# admin.site.unregister(Site)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name',
                    'last_name', 'birthday', 'gender', 'testes', 'description', 'is_staff', 'is_active')
    list_display_links = ('id', 'username')
    list_filter = ('username', 'birthday', 'testes',
                   'gender', 'is_staff', 'is_active')
    list_editable = ('is_staff',  'is_active')
    search_fields = ('testes',)
    list_per_page = 20


admin.site.register(Member, MemberAdmin)


class ScoreBloodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bloodtypeA', 'bloodtypeB', 'scorebloodtype')
    list_display_links = ('id', 'scorebloodtype')
    list_filter = ('bloodtypeA', 'bloodtypeB',)
    list_per_page = 40


admin.site.register(ScoreBloodType, ScoreBloodTypeAdmin)


class ScoreDaysOfWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'daysofweekA', 'daysofweekB', 'scoredaysofweek')
    list_display_links = ('id', 'scoredaysofweek')
    list_filter = ('daysofweekA', 'daysofweekB',)
    list_per_page = 50


admin.site.register(ScoreDaysOfWeek, ScoreDaysOfWeekAdmin)
# admin.site.register(ScoreDaysOfWeek)


class ScoreNakSusAdmin(admin.ModelAdmin):
    list_display = ('id', 'naksusA', 'naksusB', 'scorenaksus')
    list_display_links = ('id', 'scorenaksus')
    list_filter = ('naksusA', 'naksusB',)
    list_per_page = 150


admin.site.register(ScoreNakSus, ScoreNakSusAdmin)


class ScoreRaSiAdmin(admin.ModelAdmin):
    list_display = ('id', 'rasiA', 'rasiB', 'scorerasi')
    list_display_links = ('id', 'scorerasi')
    list_filter = ('rasiA', 'rasiB',)
    list_per_page = 150


admin.site.register(ScoreRaSi, ScoreRaSiAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'age', 'daysofweek',
                    'rasi', 'bloodtype', 'naksus', 'profile_score',)
    list_display_links = ('id', 'member')
    list_filter = ('member', 'age', 'bloodtype', 'naksus', 'daysofweek')
    list_editable = ('profile_score',)
    search_fields = ('age',)
    list_per_page = 50


admin.site.register(Profile, ProfileAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'matcher1', 'matcher2', 'rating')
    list_display_links = ('id', 'matcher1')
    list_filter = ('matcher1', 'matcher2', 'rating')
    list_per_page = 50


admin.site.register(Match, MatchAdmin)


class NoMatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomatcher1', 'nomatcher2', 'rating')
    list_display_links = ('id', 'nomatcher1')
    list_filter = ('nomatcher1', 'nomatcher2', 'rating')
    list_per_page = 50


admin.site.register(NoMatch, NoMatchAdmin)


class BloodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bloodtype')
    list_display_links = ('id',)
    list_per_page = 50


admin.site.register(BloodType, BloodTypeAdmin)


class DaysOfWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'daysofweek')
    list_display_links = ('id',)
    list_per_page = 50


admin.site.register(DaysOfWeek, DaysOfWeekAdmin)


class NakSusAdmin(admin.ModelAdmin):
    list_display = ('id', 'naksus')
    list_display_links = ('id',)
    list_per_page = 50


admin.site.register(NakSus, NakSusAdmin)


class RaSiAdmin(admin.ModelAdmin):
    list_display = ('id', 'rasi')
    list_display_links = ('id',)
    list_per_page = 50


admin.site.register(RaSi, RaSiAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ratingUser', 'ratedUser', 'ratingPoint')
    list_display_links = ('id', 'ratingUser',)
    list_filter = ('ratingUser',  'ratedUser')
    search_fields = ('ratingUser',)
    list_per_page = 50


admin.site.register(Rating, RatingAdmin)
# admin.site.register(Handler)

# admin.site.register(Message)


# admin.site.register(Personality,PersonalityAdmin)
# admin.site.register(Gender)
# admin.site.register(Testes)
# admin.site.register(Goldmember)
# admin.site.register(Conversation)
# @admin.register(settings.AUTH_USER_MODEL,Member)
