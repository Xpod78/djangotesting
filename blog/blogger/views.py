# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, FormView

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('pass')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blogger/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'blogger/signup.html', {'form': form})
class UserPageView(View):
    
    def get(self, request):
        return render(request, 'blogger/user.html')

class LoginView(FormView):
    
    def get(self, request):
        return render(request, 'blogger/login.html')

class SignUpView(FormView):

    def get(self, request):
        return render(request, 'blogger/signup.html')



# Create your views here.
