from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

class IndexPageView(View):
    
    def get(self, request):
        return render(request, 'blogger/index.html')


