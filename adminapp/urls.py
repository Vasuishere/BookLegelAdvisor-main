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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from adminapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('/index', views.index),
    path('/logout', views.logout_admin),
    path('/contact', views.Show_contact),
    path('/appointment', views.Show_Appointment),
    path('/edit_user_appointments/<int:id>', views.edit_appointments, name='edit_user_appointments'),
    path('/demo', views.demo),
    
    path('/reviews', views.reviews),
    
    path('/clients', views.client),
    path('/add_client', views.add_or_edit_client),
    path('/add_or_edit_client/<int:pk>', views.add_or_edit_client),
    path('/delete_client/<int:id>', views.delete_client),
    # path('edit_client/<int:id>', views.edit_client, name='edit_client'),
    # path('add_new_client', views.add_new_client, name='add_new_client'),
    
    
    path('/lawyer', views.lawyers),
    path('/add_new_lawyer', views.add_new_lawyer, name='add_new_lawyer'),
    path('/delete_lawyer/<int:id>', views.delete_lawyer, name='delete_lawyer'),    
    path('/edit_lawyer/<int:id>', views.edit_lawyer, name='edit_lawyer'),
    
    path('/blog', views.blog),
    path('/add_blog', views.add_blog),
    path('/edit_blog/<int:id>', views.edit_blog),
    path('/delete_blog/<int:id>', views.delete_blog),    
    
    path('/case_studies', views.casestudies),
    path('/case_studies/add/', views.add_or_edit_case_study),
    path('/case_studies/edit/<int:pk>/', views.add_or_edit_case_study),
    
    path('/types_Law', views.types_Law),
    path('/add-types-law', views.add_or_edit_types_law),
    path('/edit_types_law/<int:id>', views.add_or_edit_types_law),
    path('/delete_types_law/<int:id>', views.delete_types_law),
        
    path('/attorneys', views.attorneys),
    path('/attorneys/add', views.add_team, name='add_attorney'),  
    path('/attorneys/edit/<int:id>', views.edit_attorneys, name='edit_attorney'),  
    path('/attorneys/delete/<int:id>', views.delete_Attorneys, name='delete_attorney'),
    
    path('/add-case-categories', views.add_or_edit_case_categories),
    path('/case_categories', views.case_catogory),
    path('/case_categories_edit/<int:id>', views.add_or_edit_case_categories),
    path('/delete_case_categories/<int:id>', views.delete_case_categories),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
