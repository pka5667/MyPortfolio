from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'home_active': 'active',
        'page_title': 'Home',
    }
    return render(request, "core/home.html", context)


def contact(request):
    context = {
        'contact_active': 'active',
        'page_title': 'Contact Me',
    }
    return render(request, "core/contact.html", context)
