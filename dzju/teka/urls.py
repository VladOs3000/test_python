from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('catalog', views.teka, name='catalog'),
    path('publish', views.publish, name='publish'),
    path('crazy', views.crazy, name='crazy'),
    path('crazy/download', views.download, name='download'),
    path('catalog/<int:pk>', views.CatalogDetailView.as_view(), name='catalog_detail'),
    path('catalog/<int:pk>', views.LoadFile.as_view(), name='load_file'),
    # re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)