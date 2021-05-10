from typing import ContextManager
from django import views
from django.http import request
from django.http.response import HttpResponseRedirect
from members.models import *
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.hashers import make_password
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.core.paginator import Paginator
from django.views import View
from django.db.models import Avg, Max, Min

def wellcome(request):
    return render(request, 'members/wellcome.html')


def logout_views(req):
    auth_logout(req)
    return redirect('/login/')


class LoginView(View):
    models_class = Member
    form_class = MemberLoginForm
    initial = {'key': 'value'}
    template_name = 'members/wellcome.html'

    def render(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('member_all')
        self.form = self.form_class(initial=self.initial)
        self.context = {'form': self.form}
        return self.render(request)

    def post(self, request, *args, **kwargs):
        next = self.request.GET.get('next')
        self.form = self.form_class(request.POST)
        self.username = request.POST.get('username', '')
        self.password = request.POST.get('password', '')
        self.user = authenticate(username=self.username, password=self.password)
        # if request.method == 'POST':
        if self.request.user.is_authenticated:
            return redirect('member_all')
        if self.user is not None:

            if self.user.is_active:
                auth_login(request, self.user)
                messages.success(request, "You have logged in!")
                if next == None:
                    return HttpResponseRedirect('/?anode=anode&cathode=cathode&min_age=&max_age=')
                return redirect(self.request.GET.get('next'))

            else:
                messages.warning(request, "Your account is disabled!")
                return redirect('/login/')
        else:
            messages.warning(
                request, "Warning!The username or password are not valid!")
            # return redirect('/login/')
        self.context ={'form':self.form}
        return self.render(request)


class RegisterView(View):
    # pass
    models_class = Member
    form_class = MemberRegisterForm
    initial = {'key': 'value'}
    template_name = 'members/register.html'

    def render(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('member_all')

        self.form = self.form_class(initial=self.initial)
        print(self.form)
        self.context = {'form': self.form}
        return self.render(request)

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST, request.FILES,)
        if self.request.user.is_authenticated:
            return redirect('member_all')

        if self.form.is_valid():
            
            self.form.save()
            self.profile_image = self.form.cleaned_data.get('profile_image')
            self.username = self.form.cleaned_data.get('username')
            messages.success(
                request, f'Your account:{self.username} has been created! Your ar now able to login.')
            return redirect('login')
        else:
            self.form = self.form_class(initial=self.initial)
            print(self.form)
        self.context = {'form': self.form}
        return self.render(request)

class ProfileView(LoginRequiredMixin,View):
    success_url = '/profile/'
    template_name = 'members/profile.html'
    models_class = Profile
    models_member_class = Member
    initial = {'key': 'value'}
    form_class = MemberProfileUpdateForm

    def redirect(self, request, *args, **kwargs):
        return redirect(self.success_url)

    
    def render(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

   
   
    def get(self, request, *args, **kwargs):
       
        self.member = self.models_class.objects.filter(id=self.request.user.id)
        self.form = self.form_class(instance=self.request.user)
        # print(self.form)
        self.context = {'form': self.form,'member':self.member}
        return self.render(request)

    def post(self, request, *args, **kwargs):
        
        self.form = self.form_class(self.request.POST,self.request.FILES,instance=self.request.user)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, "Your account has been updated!")
            return self.redirect(request)
        else:
            self.form = self.form_class(instance=self.request.user)
        context = {'form':self.form}
        return self.render(request)

class SettingsUpdateView(LoginRequiredMixin,View):
    template_name = 'members/setting.html'
    success_url = '/setting/'
    form_class = MemberSettingUpdateForm
    delete_form_class = AccountDeleteForm
    models_profile_class =Profile

    def redirect(self, request, *args, **kwargs):
        return redirect(self.success_url)

    
    def render(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

   
    def get(self, request, *args, **kwargs):
       
        self.member = self.models_profile_class.objects.filter(id=self.request.user.id)
        self.form = self.form_class(instance=self.request.user)
        # print(self.form)
        self.context = {'form': self.form,'member':self.member}
        return self.render(request)

    def post(self, request, *args, **kwargs):
        
        self.delete_form =self.delete_form_class(request.POST, instance=request.user)
        self.form = self.form_class(self.request.POST,self.request.FILES,instance=self.request.user)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, "Setting updated!")
            return self.redirect(request)
        elif self.delete_form.is_valid():
            self.user = self.request.user
            self.user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('login')
        else:
            self.form = self.MemberSettingUpdateForm(instance=request.user)
            self.delete_form = AccountDeleteForm(instance=request.user)

        context = {'form':self.form,'delete_form': self.delete_form}
        return self.render(request)




class GetRatingView(LoginRequiredMixin, View):
    models_class = Profile
    models_class_member = Member
    models_class_bloodtype = BloodType
    models_class_dayofweek = DaysOfWeek
    models_class_naksus = NakSus
    models_class_rasi = RaSi
    models_class_scorebloodtype = ScoreBloodType
    models_class_scoredayofweek = ScoreDaysOfWeek
    models_class_scorenaksus = ScoreNakSus
    models_class_scorerasi = ScoreRaSi
    models_class_match = Match
    models_class_rating = Rating
    form_class = MatchForm
    initial = {'key': 'value'}
    template_name = 'members/member_all.html'

    def get(self, request, * args, **kwargs):

        form = self.form_class(initial=self.initial)
        own = self.models_class.objects.filter(id=request.user.id)
        member_excluded = self.models_class.objects.exclude(id=request.user.id)
        bloodtype = self.models_class_bloodtype.objects.all()
        daysofweek = self.models_class_dayofweek.objects.all()
        naksus = self.models_class_naksus.objects.all()
        rasi = self.models_class_rasi.objects.all()
        scorebloodtype = self.models_class_scorebloodtype.objects.all()
        scoredaysofweek = self.models_class_scoredayofweek.objects.all()
        scorenaksus = self.models_class_scorenaksus.objects.all()
        scorerasi = self.models_class_scorerasi.objects.all()
        

        lenbloodtype = int(len(bloodtype))
        lendaysofweek = int(len(daysofweek))
        lennaksus = int(len(naksus))
        lenrasi = int(len(rasi))

        bloodtypelist = []
        daysofweeklist = []
        naksuslist = []
        rasilist = []
        allMember = []
        allrating = []

        bloodtypewhile = 0

        while bloodtypewhile <= len(scorebloodtype):
            k = lenbloodtype + bloodtypewhile
            if k <= len(scorebloodtype):
                bloodtypelist.append([scorebloodtype[j].scorebloodtype for j in range(
                    bloodtypewhile, k)])
            bloodtypewhile += lenbloodtype

        daysofweekwhile = 0
        while daysofweekwhile <= len(scoredaysofweek):
            k = lendaysofweek + daysofweekwhile
            if k <= len(scoredaysofweek):
                daysofweeklist.append([scoredaysofweek[j].scoredaysofweek for j in range(
                    daysofweekwhile, k)])

            daysofweekwhile += lendaysofweek

        naksuswhile = 0
        while naksuswhile <= len(scorenaksus):
            k = lennaksus + naksuswhile
            if k <= len(scorenaksus):
                naksuslist.append([scorenaksus[j].scorenaksus for j in range(
                    naksuswhile, k)])

            naksuswhile += lennaksus

        rasiwhile = 0
        while rasiwhile <= len(scorerasi):
            k = lenrasi + rasiwhile
            if k <= len(scorerasi):
                rasilist.append([scorerasi[j].scorerasi for j in range(
                    rasiwhile, k)])

            rasiwhile += lenrasi

        for i in range(len(member_excluded)):  # 0,1,2,3,
            # print(i)

            if own[0].member.id != member_excluded[i].member.id and own[0].member.testes == member_excluded[i].member.gender and own[0].member.gender == member_excluded[i].member.testes:

                rating_score = (rasilist[own[0].rasi.id-1][member_excluded[i].rasi.id-1] + bloodtypelist[own[0].bloodtype.id-1][member_excluded[i].bloodtype.id-1] +
                                daysofweeklist[own[0].daysofweek.id-1][member_excluded[i].daysofweek.id -
                                                                       1] + naksuslist[own[0].naksus.id-1][member_excluded[i].naksus.id-1])*member_excluded[i].profile_score
                profiles = member_excluded[i]
                # allMember.append(profiles)
                # allrating.append(rating_score)

                own_id = own[0].member.id
                member_excluded_id = member_excluded[i].member.id
                countmember = []
                countmember.append(member_excluded_id)
                # print(countmember)



                own_get = self.models_class.objects.get(
                    id=request.user.id)
                member_excluded_get = get_object_or_404(
                    self.models_class, pk=member_excluded_id)
                
              
                
                try:
                    
                    Rating(member_owner=own_get, member_excluded=member_excluded_get,
                        ratingPoint=rating_score).save()
                    print(Rating(member_owner=own_get, member_excluded=member_excluded_get,
                        ratingPoint=rating_score))
          
                except :
              
                    # print("____________________________")
                    
                    
                    old = self.models_class_rating.objects.filter(member_owner_id=request.user.id).order_by("-ratingPoint")
                    rating_all_get = self.models_class_rating.objects.filter(member_owner_id=request.user.id,member_excluded__member__testes=request.user.gender,member_excluded__member__gender=request.user.testes).order_by("-ratingPoint")
                    # print(rating_all_get)

                    for i in range(len(old)):
                        if old[i]  in rating_all_get:
                            self.models_class_rating.objects.filter(member_excluded_id=member_excluded_id).update(ratingPoint=rating_score)
                            # print(f'__________{old[i].member_excluded.member.username}____')
                            
                        else:
                            print(old[i].member_excluded.member.username)
                            excluded_id = old[i].id
                            self.models_class_rating.objects.filter(id=excluded_id).delete()
                

    
                    
      
                
        if 'min_age' in request.GET:
            filter_age1 = request.GET.get('min_age')
            filter_age2 = request.GET.get('max_age')
            anode = request.GET.get('anode')
            cathode = request.GET.get('cathode')
            # age_min = self.models_class.objects.all().aggregate(Max('age'))[
            #         'age__min']
            # age_max = self.models_class.objects.all().aggregate(Max('age'))[
            #         'age__max']
            # print(f'________{age_min}________{age_mex}___________')
            if filter_age1 == "":
                filter_age1 = self.models_class.objects.all().aggregate(Min('age'))[
                    'age__min']
                print(filter_age1)
            if filter_age2 == '':
                filter_age2 = self.models_class.objects.all().aggregate(Max('age'))[
                    'age__max']

            if anode is None and cathode is not None:
                cathode = -1
                filter_ages = self.models_class_rating.objects.filter(
                    member_excluded__age__range=(filter_age1, filter_age2)) & self.models_class_rating.objects.filter(member_owner_id=request.user.id,member_excluded__member__testes=request.user.gender,member_excluded__member__gender=request.user.testes) & self.models_class_rating.objects.filter(ratingPoint__lte=cathode).order_by("ratingPoint")
                # print(f'__________{anode}________/{cathode}_______')

            elif anode is not None and cathode is None:
                anode = 1
                filter_ages = self.models_class_rating.objects.filter(
                    member_excluded__age__range=(filter_age1, filter_age2)) & self.models_class_rating.objects.filter(member_owner_id=request.user.id,member_excluded__member__testes=request.user.gender,member_excluded__member__gender=request.user.testes) & self.models_class_rating.objects.filter(ratingPoint__gte=anode).order_by("-ratingPoint")
                # print(f'__________{anode}________/{cathode}_______')
            else:
                filter_ages = self.models_class_rating.objects.filter(
                    member_excluded__age__range=(filter_age1, filter_age2)).order_by("-ratingPoint") & self.models_class_rating.objects.filter(member_owner_id=request.user.id,member_excluded__member__testes=request.user.gender,member_excluded__member__gender=request.user.testes)
            
            context = {
                "filter_ages": filter_ages,
                "filter_age1":filter_age1 ,
                "filter_age2":filter_age2 ,
                }
            return render(request, self.template_name, context)

       
        rating_all = self.models_class_rating.objects.filter(member_owner_id=request.user.id,member_excluded__member__testes=request.user.gender,member_excluded__member__gender=request.user.testes).order_by("-ratingPoint")
        # print(f'_____{rating_all}________')
        
        context = {
            'form': form,
            'rating_all': rating_all,
            'own': own,
            'member_excluded': member_excluded,
    
        }

        return render(request, self.template_name, context)

    def post(self, request,  *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            print(f'________________{form}______________')
            form.save()
            member1 = form.cleaned_data.get('member1')
            member2 = form.cleaned_data.get('member2')
            ratingPoint = form.cleaned_data.get('ratingPoint')
            messages.success(
                request, f'Your has been matched!')
            return HttpResponseRedirect('/')
        else:
            print("error")

        return render(request, self.template_name, {'form': form})


class Match(LoginRequiredMixin, View):
    models_class = Profile
    initial = {'key': 'value'}
    form_class = MatchForm
    template_name = 'members/member_all.html'
    models_class_scorebloodtype = ScoreBloodType
    models_class_scoredayofweek = ScoreDaysOfWeek
    models_class_scorenaksus = ScoreNakSus
    models_class_scorerasi = ScoreRaSi
    models_class_match = Match


@login_required
def memberprofile(request, username):
    return render(request, 'members/memberprofile.html', {'user': User.objects.all().get(username=username)})


@login_required
def test_view(request):
    return render(request, 'members/test.html')

# def cathode(request):
#     return render(request, 'taffy/cathode.html')


@login_required
def match(req):
    print(f'bornborn to match')
    return render(req, 'taffy/matchedtest.html')


@login_required
def rating(req):
    #  pass
    # คะแนนจาก ตารางที่หามาทำเป็น Matrix ลิงก์ จำลอง Data
    # https://colab.research.google.com/drive/1Rnk7lSw1qkbOmp79J9w3yDdXtOe94Op7?usp=sharing

    pass
