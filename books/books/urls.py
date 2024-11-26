from django.contrib import admin
from django.urls import path, include, re_path

from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('api/v1/', include('api.urls')),
    path('auth/', include('djoser.urls')), # drf: token, jwt urls
    re_path(r'^auth/', include('djoser.urls.authtoken')), # drf: token urls
    re_path(r'^auth/', include('djoser.urls.jwt')), # drf: jwt token
]
