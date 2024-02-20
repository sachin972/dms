from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', view=views.index)
]