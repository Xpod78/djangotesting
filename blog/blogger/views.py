
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic import View, ListView, FormView
from django.template import RequestContext

from .models import Post
from .forms import PostForm

def new_entry(request):
    if request.method == "POST":
        form = PostForm()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User
            post.date_created = timezone.now()
            post.date_last_modified = timezone.now()
            post.save()
            return redirect('post_page', pk=post.pk) 
    else:
        form = PostForm()
    return render(request, 'blogger/new_entry.html', {'form': form})
	    
    return render(request, 'blogger/new_entry.html', {'form': form})

def post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogger/post.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(date_created__lte=timezone.now()).order_by('date_last_modified')
    return render(request, 'blogger/all_blogs.html', {'posts': posts})

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    return render_to_response('blogger/new_entry.html', 
                              { 'form': form }, request)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('pass')
	    first_name = form.cleaned_data.get('firstname')
	    last_name = form.cleaned_data.get('lastname')
 	    email_address = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blogger/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'blogger/signup.html', {'form': form})
class UserPageView(View):
    
    def get(self, request):
        return render(request, 'blogger/user.html')



# Create your views here.
