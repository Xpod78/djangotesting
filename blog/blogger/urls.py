from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup_page'),
    url(r'^$', auth_views.login, {'template_name': 'blogger/login.html'}, name='login'),
    url(r'^signout/', auth_views.logout, {'template_name': 'blogger/logout.html'}, name='logout'),
    url(r'^home/', views.UserPageView, name='homepage')
]
