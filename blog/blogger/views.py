# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View, ListView, FormView

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
