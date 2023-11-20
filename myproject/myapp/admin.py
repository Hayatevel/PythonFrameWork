from django.contrib import admin
from .models import PhotoLibrary, Code, MyLibrary

# Register your models here.
admin.site.register(PhotoLibrary)
admin.site.register(Code)
admin.site.register(MyLibrary)