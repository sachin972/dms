from django.urls import path
from . import views

urlpatterns = [
    path('signup/', view=views.SignUP),
    path('login/', view=views.SignIN),
    path('updateRole/', view=views.UpdateRole),
]