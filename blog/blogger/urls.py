from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login_page'),
    url(r'^signup/', views.SignUpView.as_view(), name='signup_page'),
]
