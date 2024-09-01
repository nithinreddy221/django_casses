from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments


# Create your views here.
def first_app_landingpage(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1 style="color:Red; text-align: center">Welcome To First App</h1>
</body>
</html>''')
def hello_view(request):
    return HttpResponse("welcome to django")


def second_view(request):
    return render(request=request, template_name="firstapp/second_view.html")


def third_view(request):
    data = {"title": "welcome to Django",
            "about": "Here we are learning python",
            "dt": [2, 4, 6, 8, 10, 12, 14, 16]}
    return render(request=request, template_name="firstapp/third_view.html", context=data)


def depr_data_view(request):
    dept = Departments.objects.all()
    return render(request=request, template_name="firstapp/dept_view.html", context={"dept": dept})