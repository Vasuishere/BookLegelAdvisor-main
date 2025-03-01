from django.contrib import admin
from adminapp.models import adminuser,lawyer,Education,Work_experience
from clientapp.models import clients,messages


# Register your models here.
admin.site.register(adminuser)
admin.site.register(lawyer)
admin.site.register(clients)
admin.site.register(messages)
admin.site.register(Education)
admin.site.register(Work_experience)
