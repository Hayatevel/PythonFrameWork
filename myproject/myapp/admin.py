from django.contrib import admin
from .models import PhotoLibrary, MyLibrary

# Register your models here.
admin.site.register(PhotoLibrary)
admin.site.register(MyLibrary)