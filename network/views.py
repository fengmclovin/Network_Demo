from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import UserRegistrationForm


class IndexView(View):
    def get(self, request):
        return render(request, "network/index.html")


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "network/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
        else:
            return render(request, "network/login.html", {"form": form, "message": "Invalid username and/or password."})


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect("index")


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "network/register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return render(request, "network/register.html", {"form": form})


