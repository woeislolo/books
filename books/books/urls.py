from django.contrib import admin
from django.urls import path, include, re_path

from debug_toolbar.toolbar import debug_toolbar_urls

from web import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('api/v1/', include('api.urls')),
    path('auth/', include('djoser.urls')), # drf: token, jwt urls
    re_path(r'^auth/', include('djoser.urls.authtoken')), # drf: token urls
    re_path(r'^auth/', include('djoser.urls.jwt')), # drf: jwt token
]

if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
    