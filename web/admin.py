from django.contrib import admin

# Register your models here.
from .models import Student, Major


@admin.register(Student)
class Admin(admin.ModelAdmin):
    list_display = ("std_id", "prefix", "name", "lastname", "phone", "major")
    search_fields = ("std_id", "name", "lastname", "phone", "major")
    
@admin.register(Major)
class majorAdmin(admin.ModelAdmin):
    list_display = ("name", )
    