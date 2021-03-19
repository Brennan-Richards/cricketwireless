"""cricketwireless URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    # Business-facing
    # -- Leads
    path('leads-overview', views.leads_overview, name="leads_overview"),
    path('lead-details/<int:lead_id>', views.lead_details, name="lead_details"),
    path('lead-update/<int:lead_id>', views.lead_update, name="lead_update"),
    path('<pk>/lead-delete', views.LeadDelete.as_view(), name="lead_delete"),

    # -- Lines
    path('line-create/<int:lead_id>', views.line_create, name="line_create"),
    path('line-update/<int:line_id>', views.line_update, name="line_update"),
    path('<pk>/line-delete', views.LineDelete.as_view(), name="line_delete"),

    # Client-facing
    path('contact-us', views.contact_us, name="contact_us"), # Manual lead creation, therefore no source
    path('contact-us/<str:traffic_source>', views.contact_us, name="contact_us"), # User clicked through from some source (i.e.: Facebook, IG, Craigslist, ...)
    path('contact-success/<int:lead_id>', views.contact_success, name="contact_success"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
