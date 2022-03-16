from django.contrib import admin

# Register your models here.
from .models import User, App

admin.site.register(User)
admin.site.register(App)