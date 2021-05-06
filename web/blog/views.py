from members.forms import *
from members.models import Member, Profile
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
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostView(View):
    model_class = Post
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'blog/blog_index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        post = self.model_class.objects.all()
        page = request.GET.get('page', 1)
        # print(form)
        paginator = Paginator(post, 9)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {'form':form,'posts':posts}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                print(form)
                form.instance.author = self.request.user
                form.save()
                messages.success(
                    request, f' created success!')
                return redirect('/blog/')
            else:
                form = self.form_class(instance=self.request.user)
            context = {'form':form}
            return render(request, self.template_name, context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    context_object_name = 'posts'
    paginate_by = 9
    print(context_object_name)
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
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(Member, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/blog_index.html'
#     login_url = '/blog/'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'image']

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


@login_required
def postpostviews(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'blog/post_detail.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PostForm()
    return render(request, 'blog/post_detail.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        member = Member.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(author=member, post=post, text=text).save()
        messages.success(request, "Your comment has been added successfully.")
    else:
        return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)
