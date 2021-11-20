from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    context = {'cricket_logo':0}

    return render(request, 'cricketwireless/home.html', context)

@login_required
def employee_home(request):
    context = {'cricket_logo':0}
    return render(request, "cricketwireless/employee_home.html", context)

