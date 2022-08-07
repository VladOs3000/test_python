from django.urls import path
from . import views

urlpatterns = [
    path('catalog', views.teka, name='catalog'),
    path('publish', views.publish, name='publish'),
    path('crazy', views.crazy, name='crazy'),
    path('crazy/upload', views.upload_book, name='upload_book'),
    path('catalog/<int:pk>', views.CatalogDetailView.as_view(), name='catalog_detail')
]