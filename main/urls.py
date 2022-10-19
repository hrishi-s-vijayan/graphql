from django.urls import path
from . import views


urlpatterns = [
    path('customer/',views.CustomersList.as_view()),
]