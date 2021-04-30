from typing import ContextManager
from django import views
from django.http import request
from django.http.response import HttpResponseRedirect
from members.models import *
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberRegisterForm, UserUpdateForm, ProfileUpdateForm
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

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        next = self.request.GET.get('next')
        form = self.form_class(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        # if request.method == 'POST':
        if user is not None:

            if user.is_active:
                auth_login(request, user)
                messages.success(request, "You have logged in!")
                if next == None:
                    return HttpResponseRedirect('/')
                return redirect(self.request.GET.get('next'))

            else:
                messages.warning(request, "Your account is disabled!")
                return redirect('/login/')
        else:
            messages.warning(
                request, "The username or password are not valid!")
            # return redirect('/login/')

        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    # pass
    models_class = Member
    form_class = MemberRegisterForm
    initial = {'key': 'value'}
    template_name = 'members/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES,)
        if form.is_valid():
            print(f'________________{form}______________')
            form.save()
            profile_image = form.cleaned_data.get('profile_image')
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account:{username} has been created! Your ar now able to login.')
            return redirect('login')
        else:
            form = self.form_class(initial=self.initial)
            print(form)
        return render(request, 'members/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = MemberProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)
        print(form)
        if form.is_valid():
            form.save()

            messages.success(request, "Your account has been updated!")
            return redirect('profile')

    else:
        form = MemberProfileUpdateForm(instance=request.user)
        print(form)
    context = {

        'form': form,
        'member':  Profile.objects.filter(id=request.user.id)

    }
    return render(request, 'members/profile.html', context)


@login_required
def setting_view(request):
    if request.method == 'POST':
        form = MemberSettingUpdateForm(
            request.POST,  instance=request.user)
        delete_form = AccountDeleteForm(request.POST, instance=request.user)
        print(form)
        if form.is_valid():
            form.save()

            messages.success(request, "Setting updated!")
            return redirect('setting')

        elif delete_form.is_valid():
            user = request.user
            user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('login')

    else:
        form = MemberSettingUpdateForm(instance=request.user)
        delete_form = AccountDeleteForm(instance=request.user)

    context = {
        'form': form,
        'member':  Profile.objects.filter(id=request.user.id),
        'delete_form': delete_form,
    }
    return render(request, 'members/setting.html', context)


class RatingView(LoginRequiredMixin, View):
    models_class = Profile
    models_class_bloodtype = BloodType
    models_class_dayofweek = DaysOfWeek
    models_class_naksus = NakSus
    models_class_rasi = RaSi
    models_class_scorebloodtype = ScoreBloodType
    models_class_scoredayofweek = ScoreDaysOfWeek
    models_class_scorenaksus = ScoreNakSus
    models_class_scorerasi = ScoreRaSi
    models_class_match = Match
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

            if own[0].member.id != member_excluded[i].member.id and own[0].member.testes == member_excluded[i].member.gender:

                rating = (rasilist[own[0].rasi.id-1][member_excluded[i].rasi.id-1] + bloodtypelist[own[0].bloodtype.id-1][member_excluded[i].bloodtype.id-1] +
                          daysofweeklist[own[0].daysofweek.id-1][member_excluded[i].daysofweek.id -
                                                                 1] + naksuslist[own[0].naksus.id-1][member_excluded[i].naksus.id-1])*member_excluded[i].profile_score
                profiles = member_excluded[i]

                # print(f'___{type(profiles.member.id)}____')
                # rating = get_object_or_404(Rating)
                # print(f'___{profiles}____')

                own_id = own[0].member.id
                member_excluded_id = member_excluded[i].member.id
                own_get = Member.objects.get(id=own_id)
                member_excluded_get = get_object_or_404(
                    Member, pk=member_excluded_id)
                rating_all = Rating.objects.all()
                # print(len(rating_all))
                if len(rating_all) == 0:
                    print(len(rating_all))

                    # Rating(ratingUser=own_get, ratedUser=member_excluded_get,
                    #        ratingPoint=rating).save()
                # try:
                #     test = Rating.objects.filter(id=member2.id)
                #     if member2.id == ratedUser and rating == :
                #         print('sane')
                #     else:
                #         print("no")
                #         pass
                #     print(

                #         f'print in try_______{Rating.objects.all()}_____{member2.ratingPoint}')
                # Rating(ratingUser=member, ratedUser=member2,
                #        sex_ori=member_excluded[i].member.testes, age=member_excluded[i].age, ratingPoint=rating).save()
                # except:
                #     None
                #     print(Rating.objects.filter(
                #         ratedUser__member__username=member2.username))
                # pass

                # print(member.id, member2.id, ratingUser_id, ratedUser_id)
                allMember.append(profiles)
                allrating.append(rating)

            result = zip(allMember, allrating)
            result_dict = dict(result)
            sorted_dict = {}
            sorted_dictAnode = {}
            sorted_dictCathode = {}
            # [1, 2, 3] reverse=True => 3,2,1
            sorted_keys = sorted(
                result_dict, key=result_dict.get, reverse=True)

            for w in sorted_keys:

                if result_dict[w] > 0 or result_dict[w] < 0:
                    sorted_dict[w] = result_dict[w]
                    # print(sorted_dict[w])

            for e in sorted_keys:
                if result_dict[w] > 0:

                    sorted_dictAnode[e] = result_dict[e]

            for r in sorted_keys:
                if result_dict[w] < 0:

                    sorted_dictCathode[r] = result_dict[r]

        # print(f'_____________{sorted_dict}_______________')
        # print(f'_____________{result_dict}_______________')
        # print(f'___{allMember}_______{allrating}_________')

        context = {'form': form, 'own': own,
                   'member_excluded': member_excluded,
                   'result_dict': result_dict,
                   'sorted_dict': sorted_dict,
                   'sorted_dictAnode': sorted_dictAnode,
                   'sorted_dictCathode': sorted_dictCathode,
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
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
