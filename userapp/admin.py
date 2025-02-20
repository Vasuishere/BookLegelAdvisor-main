from django.contrib import admin
from .models import Attorneys,Client_Review,Blog,Types_Law,Practice_Area,case_categories,case_studies,contact,Appointment,user,User_Appointment

# Register your models here.

admin.site.register(Attorneys)
admin.site.register(Client_Review)
admin.site.register(Blog)
admin.site.register(user)
admin.site.register(Types_Law)
admin.site.register(Practice_Area)
admin.site.register(case_studies)
admin.site.register(case_categories)
admin.site.register(contact)
admin.site.register(Appointment)
admin.site.register(User_Appointment)