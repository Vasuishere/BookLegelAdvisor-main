"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientapp import views

app_name = 'clientapp'

urlpatterns = [
    path('', views.login_client, name='login_client'),
    path('logout/', views.logout_client, name='logout_client'),
    path('index/', views.index, name='index'),
    path('appointment/', views.appoin_tment, name='appointment'),
    path('details/', views.details, name='details'),
    path('newcase/', views.newcase_view, name='newcase'),
    path('instruction/', views.instruction, name='instruction'),
    path('case_list_view/', views.instruction, name='case_list_view'),
]
