from django.contrib import admin
from .models import Lead, Line
# Register your models here.

class LeadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lead._meta.fields]
admin.site.register(Lead, LeadAdmin)

class LineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Line._meta.fields]
admin.site.register(Line, LineAdmin)