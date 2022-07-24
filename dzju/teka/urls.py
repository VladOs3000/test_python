from django.urls import path
from . import views

urlpatterns = [
    path('catalog', views.teka, name='catalog'),
    path('publish', views.publish, name='publish')
]