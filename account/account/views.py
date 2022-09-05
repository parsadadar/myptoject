import email
from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import LoginForm


def index(req):
    return render(req, 'account/home.html')


def signup(req):
    if req.method == "POST":
        username = req.POST.get('username', False)
        password = req.POST.get('password', False)
        email = req.POST.get('email', False)
        if username and password and email:
            user = User.objects.create_user(username, password, email)
            user.save()
            return redirect(req,"site/login.html")
        else:
            return redirect("sign_up")
    return render(req, "site/sign_up.html")


def user_login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                req, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(req, user)
                    return redirect(req,'account/home.html')
                else:
                    return HttpResponse('user is not active')
            else:
                return HttpResponse('information is not valid ')
    else:
        form = LoginForm()
    return render(req, 'site/login.html', {'form': form})


def log_out(req):
    logout(req)
    return render(req, 'site/logout.html')


