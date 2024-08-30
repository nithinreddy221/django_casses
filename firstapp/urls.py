from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello_view, name="hello"),
    path('sec/', second_view, name="second"),
    path('third/', third_view, name="third"),
]