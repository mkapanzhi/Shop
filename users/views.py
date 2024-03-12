from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import LoginUserForm, RegisterUserForm


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, "users/register_done.html")
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)