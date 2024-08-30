from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_view(request):
    return HttpResponse("welcome to django")


def second_view(request):
    return render(request=request, template_name="firstapp/second_view.html")


def third_view(request):
    data = {"title": "welcome to Django",
            "about": "Here we are elearning python",
            "dt": [2, 4, 6, 8, 10, 12, 14, 16]}
    return render(request=request, template_name="firstapp/third_view.html", context=data)
