
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view( # new
openapi.Info(
title="Person API",
default_version="v1",
description="HNGx second stage task",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="jpcwork081@gmail.com"),
license=openapi.License(name="BSD License"),
),
public=True,
# permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('swagger/', schema_view.with_ui( 'swagger', 
            cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)