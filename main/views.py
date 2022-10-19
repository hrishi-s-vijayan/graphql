from django.shortcuts import render

from rest_framework.views import APIView
from . import models
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

class CustomersList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = CustomerSerializer




