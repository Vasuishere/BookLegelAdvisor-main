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
from userapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signup', views.signup),
    path('about', views.about),
    path('blog', views.blog),
    path('blog-more/<int:id>', views.blog_more),
    path('contact1', views.contact1),
    path('portfolio', views.portfolio),
    path('service', views.service),
    path('single', views.single),
    path('team', views.team),
    path('appointment', views.appo_intment),
    path('login', views.login),
    path('header', views.header),
    path('logout', views.logout),
    path('law_readmore/<int:id>',views.law_readmore),
    path('read_case_studies/<int:id>',views.read_case_studies),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
