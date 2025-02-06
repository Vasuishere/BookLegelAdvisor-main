from django.contrib import admin
from adminapp.models import adminuser,lawyer
from clientapp.models import clients
from clientapp.models import messages

# Register your models here.
admin.site.register(adminuser)
admin.site.register(lawyer)
admin.site.register(clients)
admin.site.register(messages)