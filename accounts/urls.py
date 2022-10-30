from django.urls import path
from . import views

urlpatterns = [
    path('', views.signupaccount, name='signup'),
    path('logout/', views.logoutaccount,name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
    ]
