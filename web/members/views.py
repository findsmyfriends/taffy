from members.models import Message
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from .forms import *


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
        po_form = ProfileOtherUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            po_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        po_form = ProfileOtherUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'po_form': po_form,
    }
    return render(request, 'members/profile.html', context)

@login_required
def memberprofile(request, username):
    return render(request, 'taffy/memberprofile.html', {'user': User.objects.all().get(username=username)})

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

@login_required
def firstfilter(req):
    pass