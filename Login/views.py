from django.shortcuts import render, redirect
from Login.forms import RegForm, EditForm, PasswordReset, PasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import (update_session_auth_hash,
                                 login,
                                 logout,
                                 authenticate
                                 )
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'login/login.html', {"message":"Something went wrong. Please try again later!"})
        else:
            return render(request, 'login/login.html', {"message":"Your username or password seems to be wrong. Please try again!"})
    else:
        return render(request, 'login/login.html')





def register(request):
    registered = False
    user_form = RegForm()
    message = ''
    if request.method == 'POST':
        user_form = RegForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            registered = True
        else:
            message = 'Invalid password'

    return render(request, 'login/reg.html', {
        "form":user_form,
        "message":message,
        "registered":registered

    })

@login_required
def profile(request):
    args = {"user" : request.user}
    return render(request, 'login/profile.html', args)

@login_required
def edit_profile(request): # TODO: rewrite as register
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/home/profile')

    else:
        form = EditForm(instance=request.user)
        return render(request, 'login/profile_edit.html', {'form': form})

@login_required
def change_password(request): # TODO: rewrite as register
    if request.method == 'POST':
        form = PasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/home/profile')

    else:
        form = PasswordForm(user=request.user)
        return render(request, 'login/change_password.html', {'form': form})

# TODO: Complete view
def reset_password(request):
    form = PasswordReset()
    return render(request, 'registration/password_reset_form.html',{"form":form})
