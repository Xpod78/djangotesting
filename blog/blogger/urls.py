from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup_page'),
    url(r'^$', auth_views.login, {'template_name': 'blogger/login.html'}, name='login'),
    url(r'^signout/', auth_views.logout, {'template_name': 'blogger/logout.html'}, name='logout'),
    url(r'^home/', TemplateView.as_view(template_name='blogger/user.html'), name='home'),
   
]
