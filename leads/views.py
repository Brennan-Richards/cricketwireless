from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView

from .models import Lead
from .forms import ContactForm

# Create your views here.

# Business-facing
def leads_overview(request):
    context = {}
    context['leads_list'] = Lead.objects.filter(current_status__in=['Inquired', 'Contacted']).order_by('-date_created')
    for i in context['leads_list'][:3]:
        print(i.date_created)
    return render(request, "leads/business/leads_overview.html", context)


def lead_details(request, lead_id):
    context = {}
    context['lead'] = Lead.objects.get(id=lead_id)
    return render(request, "leads/business/lead_details.html", context)


def lead_update(request, lead_id):
    context = {}

    lead = Lead.objects.get(id=lead_id)
    context['lead'] = lead

    lead_update_form = ContactForm(request.POST or None, instance=lead, update=True)
    context['form'] = lead_update_form

    if lead_update_form.is_valid():
        lead = lead_update_form.save()
        return redirect('lead_details', lead_id=lead_id)

    return render(request, "leads/business/lead_update.html", context)

class LeadDelete(DeleteView):
    model = Lead
    success_url = reverse_lazy('leads_overview')
    template_name = 'leads/business/lead_confirm_delete.html'

# Client-facing

def contact_us(request, traffic_source='manual'):
    context = {}

    contact_form = ContactForm(request.POST or None, update=False)
    context['form'] = contact_form

    # Storing this value to be used in POST requests.
    t_s = traffic_source

    if contact_form.is_valid():
        lead = contact_form.save(commit=False)
        lead.source = t_s.upper()
        lead.save()
        return redirect('contact_success', lead_id=lead.id)

    return render(request, 'leads/client/contact_us.html', context)


def contact_success(request, lead_id):
    context = {}
    lead = Lead.objects.get(id=lead_id)
    context['lead'] = lead
    return render(request, "leads/client/contact_success.html")