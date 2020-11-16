from django.contrib import admin
from django.urls import path
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
    # test404
)

from django.conf import settings
from django.conf.urls.static import static


handler404 = handler404

urlpatterns = [

    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),

    # path('test/', test404, name='test'),


    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
