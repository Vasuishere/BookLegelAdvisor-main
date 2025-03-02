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
from lawyerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo', views.demo, name='demo'),
    path('pricing', views.pricing, name='pricing'),
    path('virtualappointment', views.virtualappointment, name='virtualappointment'),
    path('appointment', views.appointment, name='appointment'),
    path('profile', views.profile, name='profile'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('paymentrequest/<int:id>/', views.payment_request, name='paymentrequest'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('message/<int:id>/', views.message, name='message'),
    path('activeclient', views.activeclient, name='activeclient'),
    path('index', views.index, name='index'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('update-status/<int:appointment_id>/', views.update_status, name='update_status'),
    path('', views.login_lawyer, name='login_lawyer'),
    path('logout', views.logout_lawyer, name='logout_lawyer'),
    path('google-login-callback/', views.google_login_callback, name='google_login_callback'),
]