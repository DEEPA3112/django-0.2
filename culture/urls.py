from django.urls import path
from . import views
# ####:8000/culture
urlpatterns = [
    path('',views.simple_view)
]
