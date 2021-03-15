from django.contrib import admin
from .models import Lead
# Register your models here.

class LeadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lead._meta.fields]
admin.site.register(Lead, LeadAdmin)