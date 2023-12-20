from django.contrib import admin
from .models import Profile
# Register your models here.
# Superuser: username - admin, password - admin12

admin.site.site_header = "CV Generator Admin Panel"
admin.site.site_title = "CV Generator"
admin.site.register(Profile);