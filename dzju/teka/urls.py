from django.urls import path
from . import views

urlpatterns = [
    path('', views.teka_home, name='teka_home'),
    path('publish', views.publish, name='publish')
]