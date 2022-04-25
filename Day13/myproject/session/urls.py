
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("set/", views.setsession, name="setsession"),
    path("get/", views.getsession, name="getsession"),
    path("del/", views.delsession, name="delsession"),

    path("settime/", views.setssntime, name="setssntime"),
    path("gettime/", views.getssntime, name="getssntime"),
    path("deltime/", views.delssntime, name="delssntime"),
]

