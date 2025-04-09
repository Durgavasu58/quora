from django.contrib import admin
from .models import  Question, UserProfile, Comments
# Register your models here.

admin.site.register(Question)
admin.site.register(UserProfile)
admin.site.register(Comments)
