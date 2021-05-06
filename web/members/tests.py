from django.test import TestCase
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile,Rating
from django.db.models import Avg, Max, Min
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def tests(request):
    if 'min_age' in request.GET:
        filter_age1 = request.GET.get('min_age')
        filter_age2 = request.GET.get('max_age')
        rating = request.GET.get('rating')
        gender = request.GET.get('gender')
        anode = request.GET.get('anode')
        cathode = request.GET.get('cathode')

        if gender is None:
            gender = "M"
        if filter_age1 == "":
            filter_age1 = 0
        if filter_age2 == '':
            filter_age2 = Profile.objects.all().aggregate(Max('age'))[
                'age__max']

        if anode is None and cathode is not None:
            cathode = -1
            ages = Rating.objects.filter(
                member_excluded__age__range=(filter_age1, filter_age2)) & Rating.objects.filter(member_excluded__member__gender=gender) & Rating.objects.filter(ratingPoint__lte=cathode).order_by("ratingPoint")
            print(f'__________{anode}________/{cathode}_______')

        elif anode is not None and cathode is None:
            anode = 1
            ages = Rating.objects.filter(
                member_excluded__age__range=(filter_age1, filter_age2)) & Rating.objects.filter(member_excluded__member__gender=gender) & Rating.objects.filter(ratingPoint__gte=anode).order_by("-ratingPoint")
            print(f'__________{anode}________/{cathode}_______')
        else:
            ages = Rating.objects.filter(
                member_excluded__age__range=(filter_age1, filter_age2)).order_by("-ratingPoint") & Rating.objects.filter(member_excluded__member__gender=gender)
    
        
        # print(f'_________________{ages}________________')
        context = {"ages": ages}
        return render(request, 'members/test.html', context)
    profile = Rating.objects.filter(member_owner_id=request.user.id).order_by("-ratingPoint")
    print(profile)
    
    print(f'__________{profile}________')
    context = {"profile": profile}
    return render(request, 'members/test.html', context)


# class Conversation(LoginRequiredMixin, View):
#     initial = {'key': 'value'}
#     template_name = 'members/conversation.html'

#     def __init__(self,  *args, **kwargs):
#         self.models_class = Profile
#         self.models_class_scorebloodtype = ScoreBloodType
#         self.models_class_scoredayofweek = ScoreDaysOfWeek
#         self.models_class_scorenaksus = ScoreNakSus
#         self.models_class_scorerasi = ScoreRaSi
#         self.models_class_match = Match
#         self.form_class = MatchForm

#     @ login_required
#     def message(request, username):
#         currentProfile = request.user.profile
#         otherProfile = User.objects.get(username=username).profile

#         qr = Message.objects \
#             .raw('SELECT id, sender_id, text, sentDate \
#                 FROM taffy_message \
#                 WHERE sender_id = {0} AND recipient_id = {1} \
#                 UNION \
#                 SELECT id, sender_id, text, sentDate \
#                 FROM taffy_message \
#                 WHERE sender_id = {1} AND recipient_id = {0} \
#                 ORDER BY sentDate'.format(currentProfile.id, otherProfile.id))

#         messages = [(Profile.objects.get(id=m.sender_id), m.text) for m in qr]

#         if request.method == 'POST':
#             form = MessageForm(request.POST)
#             if form.is_valid():
#                 message = Message(
#                     sender=currentProfile, recipient=otherProfile, text=form.cleaned_data['text'])
#                 message.save()
#                 return redirect(request.path)
#         else:
#             form = MessageForm()

#         return render(request, 'taffy/message.html', {'messages': messages, 'form': form})
#     pass
