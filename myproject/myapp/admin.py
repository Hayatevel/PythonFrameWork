from django.contrib import admin

from .models import MyLibrary, PhotoLibrary

# Register your models here.
admin.site.register(PhotoLibrary)
admin.site.register(MyLibrary)
