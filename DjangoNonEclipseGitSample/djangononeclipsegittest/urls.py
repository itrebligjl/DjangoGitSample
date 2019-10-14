from django.urls import path
from djangononeclipsegittest import views

urlpatterns = [
    path('', views.djangononeclipsegittest, name='djangononeclipsegittest'),
]