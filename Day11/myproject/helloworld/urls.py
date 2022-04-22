
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.home, name='home'),
    path("add", views.add, name='add')
=======
    path("", views.home, name='home')
>>>>>>> origin/master
]