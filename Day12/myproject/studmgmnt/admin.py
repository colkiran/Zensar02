from django.contrib import admin
from .models import Stud
# Register your models here.

@admin.register(Stud)
class StudAdmin(admin.ModelAdmin):
    list_display = ('id', 'stud_name', 'stud_dob', 'stud_class')
