from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .models import ProfileUser
from .forms import MyUserCreationForm
# Create your views here.


def redirect_user(request):
    url = f'/phones/'
    return HttpResponseRedirect(url)


def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        redirect_url = f"{request.user.pk}"
        return HttpResponseRedirect(redirect_to=redirect_url)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/phones/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


class UserDetail(generic.DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'


class UserProfileEdit(generic.UpdateView):
    model = ProfileUser
    form_class = MyUserCreationForm
    template_name = 'edit_user.html'
    success_url = '/phones/'

    def get_object(self):
        return self.request.user.profileuser
