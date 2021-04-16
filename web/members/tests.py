from django.test import TestCase

# Create your tests here.
""" ลอง
class MemberProfileDetailView(DetailView):
    model = Member
    template_name = 'members/profile.html'
    context_object_name = 'member'


class MemberProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Member
    fields = ['first_name', 'last_name',
              'birthday', 'bloodtype', 'profile_image']
    template_name = 'members/profile.html'

    def form_valid(self, form):
        form.instance.member = self.request.member
        print(form.instance.member)
        return super().form_valid(form)

    def test_func(self):
        member = self.get_object()
        if self.request.username == self.request.member:
            return True
        return False


class MemberDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Member
    success_url = '/login/'

    def test_func(self):
        member = self.get_object()
        if self.request.member == request.username:
            return True
        return False





class MemberProfileUpdateView(LoginRequiredMixin, View):

    models_class = Member
    models_class_profile = Profile
    form_class = MemberProfileUpdateForm
    template_name = 'members/test.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST, request.FILES, instance=request.user)
        member = self.models_class_profile.objects.filter(id=request.user.id)
        print(form)
        context = {'form': form, 'member': member}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.seve()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your account has been updated!")
            return redirect('profile')
        else:
            form = self.form_class(request.POST, instance=request.user)
            messages.success(request, "Your account hasn't been updated!")
            update_session_auth_hash(request, request.user)

        context = {
            'form': form,
            'member': Profile.objects.filter(id=request.user.id)

        }

        return render(request, self.template_name, context)



class ShowProfileAllView(View):
    model = Profile
    template_name = 'members/test.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.all()
        member = Profile.objects.filter(member__id=1).first()
        context['member'] = member
        context['profile'] = profile
        print(context)
        return context
"""
