from typing import ContextManager
from django import views
from django.http import request
from django.http.response import HttpResponseRedirect
from members import models
from members.models import BloodType, Match, Message, ScoreBloodType, ScoreDaysOfWeek, ScoreNakSus, ScoreRaSi
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
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
        print(form)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if request.method == 'POST':
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    messages.success(request, "You have logged in!")
                    return redirect('/')
                else:
                    messages.warning(request, "Your account is disabled!")
                    return redirect('/login/')
            else:
                messages.warning(
                    request, "The username or password are not valid!")
                return redirect('/login/')
                # <process form cleaned data>
            # return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


def register(request):
    if request.method == 'POST':
        form = MemberRegisterForm(request.POST, request.FILES,)
        if form.is_valid():
            print(f'________________{form}______________')
            form.save()
            profile_image = form.cleaned_data.get('profile_image')
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account:{username} has been created! Your ar now able to login.')
            return redirect('login')
            # return render(request, 'members/login.html', {'form': form,'profile_image':profile_image})
    else:

        form = MemberRegisterForm()
    return render(request, 'members/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        # po_form = ProfileOtherUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # po_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # po_form = ProfileOtherUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        # 'po_form': po_form,
    }
    return render(request, 'members/profile.html', context)


@login_required
def memberprofile(request, username):
    return render(request, 'members/memberprofile.html', {'user': User.objects.all().get(username=username)})


@login_required
def testtem(request):
    return render(request, 'members/testswipe.html')

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

    rasi = [[3, 2, -3, 0, 3, -3, -1, -2, 0, 2, 3, 1],
            [1, 3, 2, 2, -3, 3, -1, -3, -2, -3, -3, 0],
            [0, 0, -3, -3, 2, -1, 3, -3, 3, -3, 3, 2],
            [0, -2, 1, 3, -3, 3, 2, 3, -2, -3, -1, 3],
            [3, -1, 3, 1, 3, 1, 3, 2, 3, -2, -1, -3],
            [0, 3, 2, -1, -2, 3, -3, 3, 2, 3, 0, 3],
            [-2, -3, -1, -3, 3, -2, 3, 2, 3, 0, 3, 0],
            [-3, -2, 2, 3, 1, 3, 0, 3, -1, -2, 3, -1],
            [3, 3, -2, 3, 1, 3, 2, 2, -2, -3, -2, -3],
            [2, 3, -2, -3, -1, 3, -2, -3, -1, 2, 2, -1],
            [3, 1, 3, -3, -2, 0, 0, 0, 3, 2, 3, 1],
            [-3, -2, -2, 3, 1, -3, 2, 3, 2, 3, 1, 0]]
    range_age = [[-1, 1, 2, 0, -2, 1, -2],
                 [2, 0, 2, -1, 2, 2, 2],
                 [2, 1, 0, 1, 2, 2, 1],
                 [-2, -1, 2, 0, 2, -2, 0],
                 [-2, -1, 0, 2, 2, -2, -1],
                 [1, 0, -1, -1, 2, 0, -2],
                 [-1, -2, 0, -1, 2, -2, -2]]
    bloodtype = [[2, 0, 1, -1], [1, 2, 2, -1], [1, -1, 2, 2], [-1, 0, 1, 2]]
    daysofweek = [[-1, 0, 1, -1, -1, 0, -2, 1],
                  [-3, -1, 0, 1, -3, -3, -2, 3],
                  [-3, 1, 1, 1, 1, -3, 3, 3],
                  [-1, 3, 3, 3, 2, -1, -2, 2],
                  [3, 1, 3, -3, -3, 1, -1, -2],
                  [2, 2, -1, -1, -2, 3, -1, -2],
                  [3, -2, 1, -1, -2, -2, 2, 0],
                  [3, -3, 3, 0, -2, 3, 0, 2]]
    naksus = [[-4, 1, -1, 3, 4, 3, 1, -1, -1, 0, 0, 4],
              [-4, 1, 1, -1, 3, 3, 0, 4, -1, 1, -4, -1],
              [2, -3, -3, 2, -4, 4, -1, 0, 2, 3, 4, 1],
              [-3, -4, 1, -4, -4, -2, 4, -3, 0, -2, -3, 2],
              [-3, 2, 4, 1, 1, 2, 0, 0, 3, -3, -4, 1],
              [2, 3, -3, 1, 4, -1, -3, -1, 2, 1, 1, -4],
              [0, 2, 3, 3, 0, -1, 3, 2, 4, 0, 2, -2],
              [-4, -3, -3, 1, -4, 2, 2, 2, 2, 4, 3, -2],
              [1, -3, -3, -2, 2, 1, 4, -2, -1, -3, 1, -3],
              [4, 0, 3, 2, -1, 3, 4, -3, -3, -3, 4, -3],
              [4, -4, -1, -3, -1, -3, 3, -4, -3, 3, -4, 3],
              [-4, -2, -4, 2, -4, 4, -1, 1, 0, 0, -3, 0]]

    allMember = []
    allrating = []
    data = []
    data2 = []
    # userA = Profile.objects.filter(user__id=1).first()
    userA = Profile.objects.filter(user__id=req.user.id).first()
    allprofile = Profile.objects.all()
    if userA.rasi and userA.bloodtype and userA.daysofweek and userA.naksus is not None:
        for i in range(len(Profile.objects.all())):  # 0,1,2,3,
            if userA.user.id is not allprofile[i].id and userA.testes is allprofile[i].gender:
                userB = Profile.objects.filter(user__id=i+1).first()
                rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1] + \
                    daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1] + \
                    naksus[userA.naksus.id-1][userB.naksus.id-1]
                profiles = allprofile[i]
                allMember.append(profiles)
                allrating.append(rating)

        result = zip(allMember, allrating)
        result_dict = dict(result)
        sorted_dict = {}
        sorted_dictAnode = {}
        sorted_dictCathode = {}
        # [1, 2, 3] reverse=True => 3,2,1
        sorted_keys = sorted(result_dict, key=result_dict.get, reverse=True)

        for w in sorted_keys:

            sorted_dict[w] = result_dict[w]

        for e in sorted_keys:
            if result_dict[w] > 0:

                sorted_dictAnode[e] = result_dict[e]

        for r in sorted_keys:
            if result_dict[w] < 0:

                sorted_dictCathode[r] = result_dict[r]

        print(sorted_keys)

        return render(req, 'taffy/index.html', {
            'data': data,
            'data2': data2,
            'result_dict': result_dict,
            'userA': userA,
            'userB': userB,
            'sorted_dict': sorted_dict,
            'sorted_dictAnode': sorted_dictAnode,
            'sorted_dictCathode': sorted_dictCathode,



        })
    else:
        print("else")

        if req.method == 'POST':
            uuu_form = UserUpdateForm(req.POST, instance=req.user)
            ppp_form = ProfileUpdateForm(
                req.POST, req.FILES, instance=req.user.profile)

            if uuu_form.is_valid() and ppp_form.is_valid():
                uuu_form.save()
                ppp_form.save()
                # po_form.save()
                messages.success(req, "Your account has been updated!")
                return redirect('profile')

        else:
            uuu_form = UserUpdateForm(instance=req.user)
            ppp_form = ProfileUpdateForm(instance=req.user.profile)
            # po_form = ProfileOtherUpdateForm(instance=req.user.profile)

        context = {
            'uuu_form': uuu_form,
            'ppp_form': ppp_form,

        }
        return render(req, 'members/filter.html', context)


@login_required
def anode(req):
    #  pass
    # คะแนนจาก ตารางที่หามาทำเป็น Matrix ลิงก์ จำลอง Data
    # https://colab.research.google.com/drive/1Rnk7lSw1qkbOmp79J9w3yDdXtOe94Op7?usp=sharing

    rasi = [[3, 2, -3, 0, 3, -3, -1, -2, 0, 2, 3, 1],
            [1, 3, 2, 2, -3, 3, -1, -3, -2, -3, -3, 0],
            [0, 0, -3, -3, 2, -1, 3, -3, 3, -3, 3, 2],
            [0, -2, 1, 3, -3, 3, 2, 3, -2, -3, -1, 3],
            [3, -1, 3, 1, 3, 1, 3, 2, 3, -2, -1, -3],
            [0, 3, 2, -1, -2, 3, -3, 3, 2, 3, 0, 3],
            [-2, -3, -1, -3, 3, -2, 3, 2, 3, 0, 3, 0],
            [-3, -2, 2, 3, 1, 3, 0, 3, -1, -2, 3, -1],
            [3, 3, -2, 3, 1, 3, 2, 2, -2, -3, -2, -3],
            [2, 3, -2, -3, -1, 3, -2, -3, -1, 2, 2, -1],
            [3, 1, 3, -3, -2, 0, 0, 0, 3, 2, 3, 1],
            [-3, -2, -2, 3, 1, -3, 2, 3, 2, 3, 1, 0]]
    range_age = [[-1, 1, 2, 0, -2, 1, -2],
                 [2, 0, 2, -1, 2, 2, 2],
                 [2, 1, 0, 1, 2, 2, 1],
                 [-2, -1, 2, 0, 2, -2, 0],
                 [-2, -1, 0, 2, 2, -2, -1],
                 [1, 0, -1, -1, 2, 0, -2],
                 [-1, -2, 0, -1, 2, -2, -2]]
    bloodtype = [[2, 0, 1, -1],
                 [1, 2, 2, -1],
                 [1, -1, 2, 2],
                 [-1, 0, 1, 2]]
    daysofweek = [[-1, 0, 1, -1, -1, 0, -2, 1],
                  [-3, -1, 0, 1, -3, -3, -2, 3],
                  [-3, 1, 1, 1, 1, -3, 3, 3],
                  [-1, 3, 3, 3, 2, -1, -2, 2],
                  [3, 1, 3, -3, -3, 1, -1, -2],
                  [2, 2, -1, -1, -2, 3, -1, -2],
                  [3, -2, 1, -1, -2, -2, 2, 0],
                  [3, -3, 3, 0, -2, 3, 0, 2]]
    naksus = [[-4, 1, -1, 3, 4, 3, 1, -1, -1, 0, 0, 4],
              [-4, 1, 1, -1, 3, 3, 0, 4, -1, 1, -4, -1],
              [2, -3, -3, 2, -4, 4, -1, 0, 2, 3, 4, 1],
              [-3, -4, 1, -4, -4, -2, 4, -3, 0, -2, -3, 2],
              [-3, 2, 4, 1, 1, 2, 0, 0, 3, -3, -4, 1],
              [2, 3, -3, 1, 4, -1, -3, -1, 2, 1, 1, -4],
              [0, 2, 3, 3, 0, -1, 3, 2, 4, 0, 2, -2],
              [-4, -3, -3, 1, -4, 2, 2, 2, 2, 4, 3, -2],
              [1, -3, -3, -2, 2, 1, 4, -2, -1, -3, 1, -3],
              [4, 0, 3, 2, -1, 3, 4, -3, -3, -3, 4, -3],
              [4, -4, -1, -3, -1, -3, 3, -4, -3, 3, -4, 3],
              [-4, -2, -4, 2, -4, 4, -1, 1, 0, 0, -3, 0]]

    allMember = []
    allrating = []
    data = []
    data2 = []
    # userA = Profile.objects.filter(user__id=1).first()
    userA = Profile.objects.filter(user__id=req.user.id).first()
    allprofile = Profile.objects.all()
    for i in range(len(Profile.objects.all())):  # 0,1,2,3,
        if userA.user.id is not allprofile[i].id and userA.testes is allprofile[i].gender:
            userB = Profile.objects.filter(user__id=i+1).first()
            rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1] + \
                daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1] + \
                naksus[userA.naksus.id-1][userB.naksus.id-1]
            profiles = allprofile[i]
            allMember.append(profiles)
            allrating.append(rating)

    result = zip(allMember, allrating)
    result_dict = dict(result)
    sorted_dict = {}
    # [1, 2, 3] reverse=True => 3,2,1
    sorted_keys = sorted(result_dict, key=result_dict.get, reverse=True)
    filter = []
    for w in sorted_keys:
        if result_dict[w] >= 0:
            sorted_dict[w] = result_dict[w]

        print("for w in sorted_keys:", w, "result_dict[w]:", result_dict[w])
        # filter.append(sorted_dict[w])
    print(sorted_keys)
    print(filter)

    return render(req, 'members/anode.html', {
        'data': data,
        'data2': data2,
        'result_dict': result_dict,
        'userA': userA,
        'userB': userB,
        'sorted_dict': sorted_dict,



    })


@login_required
def cathode(req):
    #  pass
    # คะแนนจาก ตารางที่หามาทำเป็น Matrix ลิงก์ จำลอง Data
    # https://colab.research.google.com/drive/1Rnk7lSw1qkbOmp79J9w3yDdXtOe94Op7?usp=sharing

    rasi = [[3, 2, -3, 0, 3, -3, -1, -2, 0, 2, 3, 1],
            [1, 3, 2, 2, -3, 3, -1, -3, -2, -3, -3, 0],
            [0, 0, -3, -3, 2, -1, 3, -3, 3, -3, 3, 2],
            [0, -2, 1, 3, -3, 3, 2, 3, -2, -3, -1, 3],
            [3, -1, 3, 1, 3, 1, 3, 2, 3, -2, -1, -3],
            [0, 3, 2, -1, -2, 3, -3, 3, 2, 3, 0, 3],
            [-2, -3, -1, -3, 3, -2, 3, 2, 3, 0, 3, 0],
            [-3, -2, 2, 3, 1, 3, 0, 3, -1, -2, 3, -1],
            [3, 3, -2, 3, 1, 3, 2, 2, -2, -3, -2, -3],
            [2, 3, -2, -3, -1, 3, -2, -3, -1, 2, 2, -1],
            [3, 1, 3, -3, -2, 0, 0, 0, 3, 2, 3, 1],
            [-3, -2, -2, 3, 1, -3, 2, 3, 2, 3, 1, 0]]
    range_age = [[-1, 1, 2, 0, -2, 1, -2],
                 [2, 0, 2, -1, 2, 2, 2],
                 [2, 1, 0, 1, 2, 2, 1],
                 [-2, -1, 2, 0, 2, -2, 0],
                 [-2, -1, 0, 2, 2, -2, -1],
                 [1, 0, -1, -1, 2, 0, -2],
                 [-1, -2, 0, -1, 2, -2, -2]]
    bloodtype = [[2, 0, 1, -1],
                 [1, 2, 2, -1],
                 [1, -1, 2, 2],
                 [-1, 0, 1, 2]]
    daysofweek = [[-1, 0, 1, -1, -1, 0, -2, 1],
                  [-3, -1, 0, 1, -3, -3, -2, 3],
                  [-3, 1, 1, 1, 1, -3, 3, 3],
                  [-1, 3, 3, 3, 2, -1, -2, 2],
                  [3, 1, 3, -3, -3, 1, -1, -2],
                  [2, 2, -1, -1, -2, 3, -1, -2],
                  [3, -2, 1, -1, -2, -2, 2, 0],
                  [3, -3, 3, 0, -2, 3, 0, 2]]
    naksus = [[-4, 1, -1, 3, 4, 3, 1, -1, -1, 0, 0, 4],
              [-4, 1, 1, -1, 3, 3, 0, 4, -1, 1, -4, -1],
              [2, -3, -3, 2, -4, 4, -1, 0, 2, 3, 4, 1],
              [-3, -4, 1, -4, -4, -2, 4, -3, 0, -2, -3, 2],
              [-3, 2, 4, 1, 1, 2, 0, 0, 3, -3, -4, 1],
              [2, 3, -3, 1, 4, -1, -3, -1, 2, 1, 1, -4],
              [0, 2, 3, 3, 0, -1, 3, 2, 4, 0, 2, -2],
              [-4, -3, -3, 1, -4, 2, 2, 2, 2, 4, 3, -2],
              [1, -3, -3, -2, 2, 1, 4, -2, -1, -3, 1, -3],
              [4, 0, 3, 2, -1, 3, 4, -3, -3, -3, 4, -3],
              [4, -4, -1, -3, -1, -3, 3, -4, -3, 3, -4, 3],
              [-4, -2, -4, 2, -4, 4, -1, 1, 0, 0, -3, 0]]

    allMember = []
    allrating = []
    data = []
    data2 = []
    # userA = Profile.objects.filter(user__id=1).first()
    userA = Profile.objects.filter(user__id=req.user.id).first()
    allprofile = Profile.objects.all()
    for i in range(len(Profile.objects.all())):  # 0,1,2,3,
        if userA.user.id is not allprofile[i].id and userA.testes is allprofile[i].gender:
            userB = Profile.objects.filter(user__id=i+1).first()
            rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1] + \
                daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1] + \
                naksus[userA.naksus.id-1][userB.naksus.id-1]
            profiles = allprofile[i]
            allMember.append(profiles)
            allrating.append(rating)

    result = zip(allMember, allrating)
    result_dict = dict(result)
    sorted_dict = {}
    # [1, 2, 3] reverse=True => 3,2,1
    sorted_keys = sorted(result_dict, key=result_dict.get)
    filter = []
    for w in sorted_keys:
        if result_dict[w] < 0:
            sorted_dict[w] = result_dict[w]

        print("for w in sorted_keys:", w, "result_dict[w]:", result_dict[w])
        # filter.append(sorted_dict[w])
    print(sorted_keys)
    print(filter)

    return render(req, 'members/cathode.html', {
        'data': data,
        'data2': data2,
        'result_dict': result_dict,
        'userA': userA,
        'userB': userB,
        'sorted_dict': sorted_dict,



    })


class ShowProfileAllView(View):
    model = Profile
    template_name = 'members/rete.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.all()
        member = Profile.objects.filter(member__id=1).first()
        context['member'] = member
        context['profile'] = profile
        # print(profile.id)
        for i in range(len(profile)):
            print(i)
            # if i.member.id is not member.id:
            #     context['profile'] = profile
            #     print(f'________________{i.member}____________')
            #     print(f'________________{context}____________')
        return context


class RatingView(LoginRequiredMixin, View):
    initial = {'key': 'value'}
    template_name = 'members/member_all.html'

    def __init__(self,  *args, **kwargs):
        self.models_class = Profile
        self.models_class_scorebloodtype = ScoreBloodType
        self.models_class_scoredayofweek = ScoreDaysOfWeek
        self.models_class_scorenaksus = ScoreNakSus
        self.models_class_scorerasi = ScoreRaSi
        self.models_class_match = Match
        self.form_class = MatchForm
        self.paginate_by = 1

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        own = self.models_class.objects.filter(id=request.user.id)
        member_excluded = self.models_class.objects.exclude(id=request.user.id)
        scorebloodtype = self.models_class_scorebloodtype.objects.all()
        scoredaysofweek = self.models_class_scoredayofweek.objects.all()
        scorenaksus = self.models_class_scorenaksus.objects.all()
        scorerasi = self.models_class_scorerasi.objects.all()

        bloodtype = []
        daysofweek = []
        naksus = []
        rasi = []
        allMember = []
        allrating = []
        data = []
        data2 = []
        print(len(member_excluded))
        bloodtype.append([scorebloodtype[j].scorebloodtype for j in range(
            0, int(len(scorebloodtype)/4))])

        bloodtype.append([scorebloodtype[j].scorebloodtype for j in range(
            int(len(scorebloodtype)/4), int(len(scorebloodtype)/4+4))])

        bloodtype.append([scorebloodtype[j].scorebloodtype for j in range(
            int(len(scorebloodtype)/4+4), int(len(scorebloodtype)/4+4+4))])

        bloodtype.append([scorebloodtype[j].scorebloodtype for j in range(
            int(len(scorebloodtype)/4+4+4), int(len(scorebloodtype)))])

        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            0, int(len(scoredaysofweek)/7))])

        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            int(len(scoredaysofweek)/7), 7+7)])

        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            7+7, 7+7+7)])
        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            7+7+7, 7+7+7+7)])

        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            7+7+7+7, 7+7+7+7+7)])

        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            7+7+7+7+7, 7+7+7+7+7+7)])
        daysofweek.append([scoredaysofweek[j].scoredaysofweek for j in range(
            7+7+7+7+7+7, 7+7+7+7+7+7+7)])

        naksus.append([scorenaksus[j].scorenaksus for j in range(
            0, int(len(scorenaksus)/12))])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12, 12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12, 12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12, 12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12, 12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12, 12+12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12+12, 12+12+12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12+12)])
        naksus.append([scorenaksus[j].scorenaksus for j in range(
            12+12+12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12+12+12)])

        rasi.append([scorerasi[j].scorerasi for j in range(
            0, int(len(scorerasi)/12))])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12, 12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12, 12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12, 12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12, 12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12, 12+12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12+12, 12+12+12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12+12)])
        rasi.append([scorerasi[j].scorerasi for j in range(
            12+12+12+12+12+12+12+12+12+12, 12+12+12+12+12+12+12+12+12+12+12)])

        for i in range(len(member_excluded)):  # 0,1,2,3,

            if own[0].member.id != member_excluded[i].member.id and own[0].member.testes == member_excluded[i].member.gender:

                rating = (rasi[own[0].rasi.id-1][member_excluded[i].rasi.id-1] + bloodtype[own[0].bloodtype.id-1][member_excluded[i].bloodtype.id-1] +
                          daysofweek[own[0].daysofweek.id-1][member_excluded[i].daysofweek.id -
                                                             1] + naksus[own[0].naksus.id-1][member_excluded[i].naksus.id-1])*member_excluded[i].profile_score
                profiles = member_excluded[i]

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

        # contact_list = Profile.objects.all()
        # paginator = Paginator(contact_list, 1)  # Sh
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

        context = {'form': form, 'own': own,
                   'member_excluded': member_excluded,
                   'result_dict': result_dict,
                   'sorted_dict': sorted_dict,
                   'sorted_dictAnode': sorted_dictAnode,
                   'sorted_dictCathode': sorted_dictCathode, }

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
    initial = {'key': 'value'}
    template_name = 'members/member_all.html'

    def __init__(self,  *args, **kwargs):
        self.models_class = Profile
        self.models_class_scorebloodtype = ScoreBloodType
        self.models_class_scoredayofweek = ScoreDaysOfWeek
        self.models_class_scorenaksus = ScoreNakSus
        self.models_class_scorerasi = ScoreRaSi
        self.models_class_match = Match
        self.form_class = MatchForm

    pass


class Conversation(LoginRequiredMixin, View):
    initial = {'key': 'value'}
    template_name = 'members/conversation.html'

    def __init__(self,  *args, **kwargs):
        self.models_class = Profile
        self.models_class_scorebloodtype = ScoreBloodType
        self.models_class_scoredayofweek = ScoreDaysOfWeek
        self.models_class_scorenaksus = ScoreNakSus
        self.models_class_scorerasi = ScoreRaSi
        self.models_class_match = Match
        self.form_class = MatchForm

    @ login_required
    def message(request, username):
        currentProfile = request.user.profile
        otherProfile = User.objects.get(username=username).profile

        qr = Message.objects \
            .raw('SELECT id, sender_id, text, sentDate \
                FROM taffy_message \
                WHERE sender_id = {0} AND recipient_id = {1} \
                UNION \
                SELECT id, sender_id, text, sentDate \
                FROM taffy_message \
                WHERE sender_id = {1} AND recipient_id = {0} \
                ORDER BY sentDate'.format(currentProfile.id, otherProfile.id))

        messages = [(Profile.objects.get(id=m.sender_id), m.text) for m in qr]

        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = Message(
                    sender=currentProfile, recipient=otherProfile, text=form.cleaned_data['text'])
                message.save()
                return redirect(request.path)
        else:
            form = MessageForm()

        return render(request, 'taffy/message.html', {'messages': messages, 'form': form})
    pass
