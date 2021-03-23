from collections import UserDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.fields import NullBooleanField, related
from django.utils.functional import empty
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from members.models import Match, Message
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from .forms import *
from django.views.generic import DetailView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Your account has been created! Your ar now able to login.")
            return redirect('login')
    else:
       
        form = UserRegisterForm()
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
             
    messages = [ (Profile.objects.get(id=m.sender_id), m.text) for m in qr]

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(sender = currentProfile, recipient = otherProfile, text = form.cleaned_data['text'])
            message.save()
            return redirect(request.path)
    else:
        form = MessageForm()

    return render(request, 'taffy/message.html', {'messages': messages, 'form': form})



# def cathode(request):
#     return render(request, 'taffy/cathode.html')

@login_required
def match(req):
    print(f'bornborn to match')
    return render(req,'taffy/matchedtest.html')

@login_required
def rating(req):
    #  pass
        #คะแนนจาก ตารางที่หามาทำเป็น Matrix ลิงก์ จำลอง Data 
    # https://colab.research.google.com/drive/1Rnk7lSw1qkbOmp79J9w3yDdXtOe94Op7?usp=sharing 

    
    rasi = [[3,2,-3,0,3,-3,-1,-2,0,2,3,1],
            [1,3,2,2,-3,3,-1,-3,-2,-3,-3,0],
            [0,0,-3,-3,2,-1,3,-3,3,-3,3,2],
            [0,-2,1,3,-3,3,2,3,-2,-3,-1,3],
            [3,-1,3,1,3,1,3,2,3,-2,-1,-3],
            [0,3,2,-1,-2,3,-3,3,2,3,0,3],
            [-2,-3,-1,-3,3,-2,3,2,3,0,3,0],
            [-3,-2,2,3,1,3,0,3,-1,-2,3,-1],
            [3,3,-2,3,1,3,2,2,-2,-3,-2,-3],
            [2,3,-2,-3,-1,3,-2,-3,-1,2,2,-1],
            [3,1,3,-3,-2,0,0,0,3,2,3,1],
            [-3,-2,-2,3,1,-3,2,3,2,3,1,0]]
    range_age = [[-1,1,2,0,-2,1,-2],
            [2,0,2,-1,2,2,2],
            [2,1,0,1,2,2,1],
            [-2,-1,2,0,2,-2,0],
            [-2,-1,0,2,2,-2,-1],
            [1,0,-1,-1,2,0,-2],
            [-1,-2,0,-1,2,-2,-2]]
    bloodtype = [[2,0,1,-1],
            [1,2,2,-1],
            [1,-1,2,2],
            [-1,0,1,2]] 
    daysofweek=[[-1,0,1,-1,-1,0,-2,1],
            [-3,-1,0,1,-3,-3,-2,3],
            [-3,1,1,1,1,-3,3,3],
            [-1,3,3,3,2,-1,-2,2],
            [3,1,3,-3,-3,1,-1,-2],
            [2,2,-1,-1,-2,3,-1,-2],
            [3,-2,1,-1,-2,-2,2,0],
            [3,-3,3,0,-2,3,0,2]]
    naksus=[[-4,1,-1,3,4,3,1,-1,-1,0,0,4],
            [-4,1,1,-1,3,3,0,4,-1,1,-4,-1],
            [2,-3,-3,2,-4,4,-1,0,2,3,4,1],
            [-3,-4,1,-4,-4,-2,4,-3,0,-2,-3,2],
            [-3,2,4,1,1,2,0,0,3,-3,-4,1],
            [2,3,-3,1,4,-1,-3,-1,2,1,1,-4],
            [0,2,3,3,0,-1,3,2,4,0,2,-2],
            [-4,-3,-3,1,-4,2,2,2,2,4,3,-2],
            [1,-3,-3,-2,2,1,4,-2,-1,-3,1,-3],
            [4,0,3,2,-1,3,4,-3,-3,-3,4,-3],
            [4,-4,-1,-3,-1,-3,3,-4,-3,3,-4,3],
            [-4,-2,-4,2,-4,4,-1,1,0,0,-3,0]]
    
    allMember = []
    allrating = []
    data = []
    data2 = []
    # userA = Profile.objects.filter(user__id=1).first()
    userA = Profile.objects.filter(user__id=req.user.id).first()
    allprofile = Profile.objects.all()
    if userA.birthday is None or userA.user.first_name is None or userA.user.last_name is None:
        print('userA.birthday is None:')
        if req.method == 'POST':
            uuu_form = UserFilterUpdateForm(req.POST, instance=req.user)
            ppp_form = ProfileFilterUpdateForm(req.POST, req.FILES, instance=req.user.profile)
            
            if uuu_form.is_valid() and ppp_form.is_valid():
                uuu_form.save()
                ppp_form.save()
                messages.success(req, "Your account has been updated!")
                return redirect('/')

        else:
            uuu_form = UserFilterUpdateForm(instance=req.user)
            ppp_form = ProfileFilterUpdateForm(instance=req.user.profile)
            # po_form = ProfileOtherUpdateForm(instance=req.user.profile)

        context = {
            'uuu_form': uuu_form,
            'ppp_form': ppp_form,
            
        }
        return render(req, 'members/filter.html', context)
    elif userA.rasi and userA.bloodtype and userA.daysofweek and userA.naksus is not None:
        for i in range(len(Profile.objects.all())): #0,1,2,3,
        
            if userA.user.id is not allprofile[i].id and userA.testes is allprofile[i].gender:
                userB =  Profile.objects.filter(user__id=i+1).first()
                ratingDB = Rating.objects.filter(ratedUser_id=i+1).first()
                ratingDBCount = Rating.objects.all().count()
                
                rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1]+daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1]+naksus[userA.naksus.id-1][userB.naksus.id-1]
                profiles = allprofile[i]
                print(f'________in for i________{userB.bloodtype != None}')
                # if userB.bloodlskd
                # if ratingDBCount is 0  :
                #     print(f'________userB.ID=ID.ratingDB_____{ratingDBCount}')
                #     Rating.objects.create(reqUser_id=userA.id,ratedUser_id=i+1,ratingPoint=rating)
        
                # elif ratingDBCount > 0 :
                #     print(f'________ratingDBCount > 0_____{userB.id} {ratingDB.ratedUser_id}')

                # else: 
                #     print(f'________else____{ratingDBCount}')
                    # Rating.objects.create(reqUser_id=userA.id,ratedUser_id=i+1,ratingPoint=rating)
                try:
                    Rating.objects.create(reqUser_id=userA.id,ratedUser_id=i+1,ratingPoint=rating)
                except:
                    Rating.objects.get(reqUser_id=userA.id,ratedUser_id=i+1,ratingPoint=rating)
                allMember.append(profiles)
                allrating.append(rating)
        
            
        result = zip(allMember,allrating)
        result_dict = dict(result)
        sorted_dict = {}
        sorted_dictAnode = {}
        sorted_dictCathode = {}
        sorted_keys = sorted(result_dict, key=result_dict.get,reverse=True )  # [1, 2, 3] reverse=True => 3,2,1

        for w in sorted_keys:
            
            sorted_dict[w] = result_dict[w]
            
        for e in sorted_keys:
            if result_dict[w] > 0:
            
                sorted_dictAnode[e] = result_dict[e]
            
        for r in sorted_keys:
            if result_dict[w] < 0:
            
                sorted_dictCathode[r] = result_dict[r]

        print(sorted_keys)

        return render(req,'taffy/index.html',{
            # 'userA': userA,
            # 'userB': userB,
            'data':data,
            'data2':data2,
            'result_dict' :result_dict,
            'sorted_dict' : sorted_dict,
            'sorted_dictAnode':sorted_dictAnode,
            'sorted_dictCathode':sorted_dictCathode,

            

    })
        

@login_required
def anode(req):
    #  pass
        #คะแนนจาก ตารางที่หามาทำเป็น Matrix ลิงก์ จำลอง Data 
    # https://colab.research.google.com/drive/1Rnk7lSw1qkbOmp79J9w3yDdXtOe94Op7?usp=sharing 

    
    rasi = [[3,2,-3,0,3,-3,-1,-2,0,2,3,1],
            [1,3,2,2,-3,3,-1,-3,-2,-3,-3,0],
            [0,0,-3,-3,2,-1,3,-3,3,-3,3,2],
            [0,-2,1,3,-3,3,2,3,-2,-3,-1,3],
            [3,-1,3,1,3,1,3,2,3,-2,-1,-3],
            [0,3,2,-1,-2,3,-3,3,2,3,0,3],
            [-2,-3,-1,-3,3,-2,3,2,3,0,3,0],
            [-3,-2,2,3,1,3,0,3,-1,-2,3,-1],
            [3,3,-2,3,1,3,2,2,-2,-3,-2,-3],
            [2,3,-2,-3,-1,3,-2,-3,-1,2,2,-1],
            [3,1,3,-3,-2,0,0,0,3,2,3,1],
            [-3,-2,-2,3,1,-3,2,3,2,3,1,0]]
    range_age = [[-1,1,2,0,-2,1,-2],
            [2,0,2,-1,2,2,2],
            [2,1,0,1,2,2,1],
            [-2,-1,2,0,2,-2,0],
            [-2,-1,0,2,2,-2,-1],
            [1,0,-1,-1,2,0,-2],
            [-1,-2,0,-1,2,-2,-2]]
    bloodtype = [[2,0,1,-1],
            [1,2,2,-1],
            [1,-1,2,2],
            [-1,0,1,2]] 
    daysofweek=[[-1,0,1,-1,-1,0,-2,1],
            [-3,-1,0,1,-3,-3,-2,3],
            [-3,1,1,1,1,-3,3,3],
            [-1,3,3,3,2,-1,-2,2],
            [3,1,3,-3,-3,1,-1,-2],
            [2,2,-1,-1,-2,3,-1,-2],
            [3,-2,1,-1,-2,-2,2,0],
            [3,-3,3,0,-2,3,0,2]]
    naksus=[[-4,1,-1,3,4,3,1,-1,-1,0,0,4],
            [-4,1,1,-1,3,3,0,4,-1,1,-4,-1],
            [2,-3,-3,2,-4,4,-1,0,2,3,4,1],
            [-3,-4,1,-4,-4,-2,4,-3,0,-2,-3,2],
            [-3,2,4,1,1,2,0,0,3,-3,-4,1],
            [2,3,-3,1,4,-1,-3,-1,2,1,1,-4],
            [0,2,3,3,0,-1,3,2,4,0,2,-2],
            [-4,-3,-3,1,-4,2,2,2,2,4,3,-2],
            [1,-3,-3,-2,2,1,4,-2,-1,-3,1,-3],
            [4,0,3,2,-1,3,4,-3,-3,-3,4,-3],
            [4,-4,-1,-3,-1,-3,3,-4,-3,3,-4,3],
            [-4,-2,-4,2,-4,4,-1,1,0,0,-3,0]]

    allMember = []
    allrating = []
    data = []
    data2 = []
    # userA = Profile.objects.filter(user__id=1).first()
    userA = Profile.objects.filter(user__id=req.user.id).first()
    allprofile = Profile.objects.all()
    for i in range(len(Profile.objects.all())): #0,1,2,3,
        if userA.user.id is not allprofile[i].id and userA.testes is allprofile[i].gender:
            userB =  Profile.objects.filter(user__id=i+1).first()
            rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1]+daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1]+naksus[userA.naksus.id-1][userB.naksus.id-1]
            profiles = allprofile[i]
            

            print('_____________________________________rating reqUser________________________')
            allMember.append(profiles)
            allrating.append(rating)
        
    result = zip(allMember,allrating)
    result_dict = dict(result)
    sorted_dict = {}
    sorted_keys = sorted(result_dict, key=result_dict.get,reverse=True )  # [1, 2, 3] reverse=True => 3,2,1
    filter = []
    for w in sorted_keys:
        if result_dict[w] >= 0:
            sorted_dict[w] = result_dict[w]

        print("for w in sorted_keys:",w ,"result_dict[w]:",result_dict[w] )
        # filter.append(sorted_dict[w])
    print(sorted_keys)
    print(filter)

    return render(req,'members/anode.html',{
        # 'userA': userA,
        # 'userB': userB,
        'data':data,
        'data2':data2,
        'result_dict' :result_dict,
        'sorted_dict' : sorted_dict,
       
        

})
def matched(request,pk):
    form = MatchForm(request.POST)
    try:
        if form.is_valid(): 
            form.save()
            form.cleaned_data.get('user2')
            messages.success(request, "Matched it")
        else:
            print("________","else","_____2____")   
            match = Match.objects.create(user1_id=request.user.pk,user2_id=pk)
            return redirect('/')
    except:
        print(Match.objects.get(user1_id=request.user.pk,user2_id=pk))
        return redirect('/')

    # matched = Match.objects.create(user1_id=request.user.id)
    return render(request, 'taffy/index.html')
    

@login_required
def cathode(req):
    #  pass
        #คะแนนจาก ตารางที่หามาทำเป็น Matrix ลิงก์ จำลอง Data 
    # https://colab.research.google.com/drive/1Rnk7lSw1qkbOmp79J9w3yDdXtOe94Op7?usp=sharing 

    
    rasi = [[3,2,-3,0,3,-3,-1,-2,0,2,3,1],
            [1,3,2,2,-3,3,-1,-3,-2,-3,-3,0],
            [0,0,-3,-3,2,-1,3,-3,3,-3,3,2],
            [0,-2,1,3,-3,3,2,3,-2,-3,-1,3],
            [3,-1,3,1,3,1,3,2,3,-2,-1,-3],
            [0,3,2,-1,-2,3,-3,3,2,3,0,3],
            [-2,-3,-1,-3,3,-2,3,2,3,0,3,0],
            [-3,-2,2,3,1,3,0,3,-1,-2,3,-1],
            [3,3,-2,3,1,3,2,2,-2,-3,-2,-3],
            [2,3,-2,-3,-1,3,-2,-3,-1,2,2,-1],
            [3,1,3,-3,-2,0,0,0,3,2,3,1],
            [-3,-2,-2,3,1,-3,2,3,2,3,1,0]]
    range_age = [[-1,1,2,0,-2,1,-2],
            [2,0,2,-1,2,2,2],
            [2,1,0,1,2,2,1],
            [-2,-1,2,0,2,-2,0],
            [-2,-1,0,2,2,-2,-1],
            [1,0,-1,-1,2,0,-2],
            [-1,-2,0,-1,2,-2,-2]]
    bloodtype = [[2,0,1,-1],
            [1,2,2,-1],
            [1,-1,2,2],
            [-1,0,1,2]] 
    daysofweek=[[-1,0,1,-1,-1,0,-2,1],
            [-3,-1,0,1,-3,-3,-2,3],
            [-3,1,1,1,1,-3,3,3],
            [-1,3,3,3,2,-1,-2,2],
            [3,1,3,-3,-3,1,-1,-2],
            [2,2,-1,-1,-2,3,-1,-2],
            [3,-2,1,-1,-2,-2,2,0],
            [3,-3,3,0,-2,3,0,2]]
    naksus=[[-4,1,-1,3,4,3,1,-1,-1,0,0,4],
            [-4,1,1,-1,3,3,0,4,-1,1,-4,-1],
            [2,-3,-3,2,-4,4,-1,0,2,3,4,1],
            [-3,-4,1,-4,-4,-2,4,-3,0,-2,-3,2],
            [-3,2,4,1,1,2,0,0,3,-3,-4,1],
            [2,3,-3,1,4,-1,-3,-1,2,1,1,-4],
            [0,2,3,3,0,-1,3,2,4,0,2,-2],
            [-4,-3,-3,1,-4,2,2,2,2,4,3,-2],
            [1,-3,-3,-2,2,1,4,-2,-1,-3,1,-3],
            [4,0,3,2,-1,3,4,-3,-3,-3,4,-3],
            [4,-4,-1,-3,-1,-3,3,-4,-3,3,-4,3],
            [-4,-2,-4,2,-4,4,-1,1,0,0,-3,0]]

    allMember = []
    allrating = []
    data = []
    data2 = []
    # userA = Profile.objects.filter(user__id=1).first()
    userA = Profile.objects.filter(user__id=req.user.id).first()
    allprofile = Profile.objects.all()
    for i in range(len(Profile.objects.all())): #0,1,2,3,
        if userA.user.id is not allprofile[i].id and userA.testes is allprofile[i].gender:
            userB =  Profile.objects.filter(user__id=i+1).first()
            print("rasi",userB.rasi.id)
            rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1]+daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1]+naksus[userA.naksus.id-1][userB.naksus.id-1]
            profiles = allprofile[i]
            allMember.append(profiles)
            allrating.append(rating)
        
    result = zip(allMember,allrating)
    result_dict = dict(result)
    sorted_dict = {}
    sorted_keys = sorted(result_dict, key=result_dict.get)  # [1, 2, 3] reverse=True => 3,2,1
    filter = []
    for w in sorted_keys:
        if result_dict[w] < 0:
            sorted_dict[w] = result_dict[w]

        print("for w in sorted_keys:",w ,"result_dict[w]:",result_dict[w] )
        # filter.append(sorted_dict[w])
    print(sorted_keys)
    print(filter)

    return render(req,'members/cathode.html',{
        # 'userA': userA,
        # 'userB': userB,
        'data':data,
        'data2':data2,
        'result_dict' :result_dict,
        'sorted_dict' : sorted_dict,
       
        

})

class ProfileDetailView(DetailView):
    # pass
 
    model = Profile


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user1 = self.request.user
        return super().form_valid(form)

class MatchDetailView(DetailView):
    model = Match

def testtem(request):
    profile =  Profile.objects.all()
    matcher = Match.objects.all()
    for i in profile:
        print(i.id)
        # for j in matcher:
        #     print(j.user2.id)
        # if i.id == j.user2.id:
        #     profile =  Profile.objects.all()
    return render(request, 'members/testswipe.html',{'profile':profile})

def testmatch(request,pk):
    # match = Match.objects.create(user1_id=request.user.id)
    profile = Profile.objects.get(pk=pk)
    form = MatchForm(request.POST)
    try:
        if form.is_valid(): 
            form.save()
            user2 = form.cleaned_data.get('user2')

            messages.success(request, "Matched it")
        else:
            print("________","else","_____2____")   
            match = Match.objects.create(user1_id=request.user.pk,user2_id=pk)
            return redirect('/testtem/')
    except:
         Match.objects.gat(user1_id=request.user.pk,user2_id=pk)
        

    # matched = Match.objects.create(user1_id=request.user.id)
    return render(request, 'members/testswipe.html')