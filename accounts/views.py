from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .models import ProfileUser
# Create your views here.


def redirect_user(request):
    url = f'/phones/'
    return HttpResponseRedirect(url)


def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        redirect_url = f"{request.user.id}"
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
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'


class UserProfileEdit(generic.DetailView):
    model = ProfileUser
    form_class = UserCreationForm
    template_name = 'user_profile_detail.html'
    success_url = '/phones/'
    context_object_name = 'user-edit'


# def logout_view(request):
#     logout(request)
#     redirect_url = f'/phones/'
#     return HttpResponseRedirect(redirect_to=redirect_url)