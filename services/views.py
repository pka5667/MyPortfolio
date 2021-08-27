from django.shortcuts import render


# Create your views here.
def services(request):
    context = {
        'services_active': 'active',
        'page_title': 'Services',
    }
    return render(request, "services.html", context)