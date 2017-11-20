# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate

from django.test import TestCase
from django.test import Client

# Testing logins
class Test(TestCase):
    
    def test_login(self):
	user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/blogger/home', follow=True)
        user = User.objects.get(username='temporary')
        self.assertEqual(response.context['user'].email, 'temporary@gmail.com')
