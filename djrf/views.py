from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing teacher instances.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
