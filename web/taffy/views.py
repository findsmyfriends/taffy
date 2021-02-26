from members.views import profile
from members.models import Profile
from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

class ProfileListView(ListView):
    model = Profile
    template_name = 'taffy/index.html'
    context_object_name = 'profiles'
    paginate_by = 1

    

    
class PostListView(ListView):
    model = Post
    template_name = 'taffy/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        try:
            keyword = self.request.GET['q']
        except:
            keyword = ''
        if (keyword != ''):
            object_list = self.model.objects.filter(
                Q(user__icontains=keyword) | Q(age__icontains=keyword))
        else:
            object_list = self.model.objects.all()
        return object_list


class UserPostListView(ListView):
    model = Post
    template_name = 'taffy/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'taffy/about.html', {'title': 'About'})



@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(author=user, post=post, text=text).save()
        messages.success(request, "Your comment has been added successfully.")
    else:
        return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)

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
    for i in range(len(Profile.objects.all())): #0,1,2,3,
        if userA.user.id is not allprofile[i].id:
            userB =  Profile.objects.filter(user__id=i+1).first()
            rating = rasi[userA.rasi.id-1][userB.rasi.id-1] + bloodtype[userA.bloodtype.id-1][userB.bloodtype.id-1]+daysofweek[userA.daysofweek.id-1][userB.daysofweek.id-1]+naksus[userA.naksus.id-1][userB.naksus.id-1]
            profiles = allprofile[i]
            allMember.append(profiles)
            allrating.append(rating/4*100)
    result = zip(allMember,allrating)
    result_dict = dict(result)
    sorted_dict = {}
    sorted_keys = sorted(result_dict, key=result_dict.get,reverse=True)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = result_dict[w]

    # print(sorted_dict)
    return render(req,'taffy/index.html',{
        'data':data,
        'data2':data2,
        'result_dict' :result_dict,
        'userA': userA,
        'userB': userB,
        'sorted_dict' : sorted_dict,
        

})
    
