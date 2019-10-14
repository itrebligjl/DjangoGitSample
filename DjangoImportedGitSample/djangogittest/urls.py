from django.urls import path
from djangogittest import views

urlpatterns = [
    path('', views.djangogittest, name='djangogittest'),
]