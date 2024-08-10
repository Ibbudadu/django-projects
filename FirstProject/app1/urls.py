from django.urls import path

from FirstProject.app1 import views

urlpatterns = [
  path('',views.home)
]