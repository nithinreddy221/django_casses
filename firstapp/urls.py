from django.urls import path
from .views import *

urlpatterns = [
    path('', first_app_landingpage, name="fa_lp"),
    path('hello/', hello_view, name="hello"),
    path('sec/', second_view, name="second"),
    path('third/', third_view, name="third"),
    path('dept/', depr_data_view, name="dept")
]