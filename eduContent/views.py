from django.shortcuts import render


# Create your views here.
def skills(request):
    context = {
        'skills_active': 'active',
        'page_title': 'Skills',
    }
    return render(request, "eduContent/skill.html", context)
