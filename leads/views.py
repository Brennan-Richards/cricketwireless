from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView

from .models import Lead, Line
from django.contrib.auth.models import User

from .forms import ContactForm, EmployeeLeadForm, LineForm

from .utils import outreach_links
from .data_utils import *

from django.utils import timezone
from datetime import timedelta

# Create your views here.

# Business-facing
def leads_overview(request):
    context = {}
    context['leads_list'] = Lead.objects.filter(current_status__in=['Inquired', 'Contacted']).order_by('-date_created')

    next_15_days = (timezone.now(), timezone.now() + timedelta(days=15))
    context['upcoming_upgrades'] = Line.objects.filter(lead__current_status__in=['Inquired', 'Contacted', 'Sold'], upgrade_eligibility_date__range=next_15_days)

    context['outreach_links'] = outreach_links(employee_id=request.user.id)

    return render(request, "leads/business/leads_overview.html", context)


def lead_details(request, lead_id):
    context = {}
    context['lead'] = Lead.objects.get(id=lead_id)

    context['lines'] = Line.objects.filter(lead=context['lead'])

    return render(request, "leads/business/lead_details.html", context)


def lead_update(request, lead_id):
    context = {}

    lead = Lead.objects.get(id=lead_id)
    context['lead'] = lead

    lead_update_form = EmployeeLeadForm(request.POST or None, instance=lead, update=True)
    context['form'] = lead_update_form

    # Track the lead's 'current_status' before updating in order to mark 'date_sold'
    # if lead becomes sold.
    status_before_update = lead.current_status

    if request.method == 'POST':
        if lead_update_form.is_valid():
            lead_updated = lead_update_form.save(commit=False)

            # If lead was just updated to be marked as 'current_status' being 'Sold'
            if status_before_update != 'Sold' and lead_updated.current_status == 'Sold':
                lead_updated.date_sold = timezone.now()

            lead_updated.save()

            return redirect('lead_details', lead_id=lead_id)

    return render(request, "leads/business/lead_update.html", context)


class LeadDelete(DeleteView):
    model = Lead
    success_url = reverse_lazy('leads_overview')
    template_name = 'leads/business/lead_confirm_delete.html'


def line_create(request, lead_id):
    context = {}

    context['lead'] = Lead.objects.get(id=lead_id)

    line_form = LineForm(request.POST or None, update=False)
    context['form'] = line_form

    if request.method == 'POST':
        if line_form.is_valid():
            line = line_form.save(commit=False)
            line.lead = context['lead']
            line.save()
            return redirect('lead_details', lead_id=lead_id)
        else:
            print(line_form.errors)

    return render(request, 'leads/business/line_create.html', context)


def line_update(request, line_id):
    context = {}

    context['line'] = Line.objects.get(id=line_id)
    context['lead'] = context['line'].lead

    line_update_form = LineForm(request.POST or None, instance=context['line'], update=False)
    context['form'] = line_update_form

    if request.method == 'POST':
        if line_update_form.is_valid():
            line = line_update_form.save(commit=False)
            line.lead = context['lead']
            line.save()
            return redirect('lead_details', lead_id=context['line'].lead)
        else:
            print(line_update_form.errors)

    return render(request, 'leads/business/line_create.html', context)


class LineDelete(DeleteView):
    model = Line
    template_name = 'leads/business/line_confirm_delete.html'

    def get_success_url(self):
        lead = self.object.lead
        return reverse_lazy('lead_details', kwargs={'lead_id': lead.id})


# Data analysis

import plotly.graph_objects as go
import plotly.offline as plt

def data_analysis(request, time_period=None):
    context = {}

    traffic_source_data, rev_generated, proportion_sold, leads_time_series = retrieve_lead_data(15)

    context['revenue_generated'], context['proportion_sold'] = rev_generated, proportion_sold

    # Leads by traffic source pie chart.
    labels = [s for s in traffic_source_data.keys()]
    values = [v for v in traffic_source_data.values()]
    traffic_source_pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values)])
    traffic_source_pie_chart.update_layout(title="Leads by traffic source", legend_title="Traffic source", width=400, height=400)
    context['traffic_source_pie_chart'] = plt.plot(traffic_source_pie_chart, output_type='div', config={'displaylogo': False})

    # Leads time series line chart.
    sold = leads_time_series['sold']
    created = leads_time_series['created']
    leads_time_series = go.Figure()
    leads_time_series.add_trace(go.Scatter(x=[k for k in sold.keys()], y=[v for v in sold.values()],
                        mode='lines+markers',
                        name='Leads sold'))
    leads_time_series.add_trace(go.Scatter(x=[k for k in created.keys()], y=[v for v in created.values()],
                        mode='lines+markers',
                        name='Leads created'))
    leads_time_series.update_layout(title="Leads created/sold over past 15 days", legend_title="Created/sold", height=550)
    context['leads_time_series'] = plt.plot(leads_time_series, output_type='div', config={'displaylogo': False})

    # print("LEADS = ", leads)
    # print("REVENUE GENERATED = ", rev)
    # print("PROP. SOLD = ", proportion)
    # print("L.T.S. = ", lts)

    return render(request, 'leads/business/data_analysis.html', context)

# Client-facing

def contact_us(request, traffic_source='manual', employee_id=None):
    context = {}

    if not request.user.is_authenticated:
        contact_form = ContactForm(request.POST or None, update=False)
    else:
        contact_form = EmployeeLeadForm(request.POST or None, update=False)

    context['form'] = contact_form

    # Storing this value to be used in POST requests.
    t_s = traffic_source

    if request.method == 'POST':
        if contact_form.is_valid():
            lead = contact_form.save(commit=False)
            lead.source = t_s.upper().replace('_', ' ')

            # This lead can be attributed to a specific employee's outreach action.
            # the default value for the field shown here is None
            if employee_id is not None:
                lead.employee_generated_by = User.objects.get(id=employee_id)

            lead.save()
            return redirect('contact_success', lead_id=lead.id)
        else:
            print(contact_form.errors)

    return render(request, 'leads/client/contact_us.html', context)


def contact_success(request, lead_id):
    context = {}
    lead = Lead.objects.get(id=lead_id)
    context['lead'] = lead
    return render(request, "leads/client/contact_success.html")