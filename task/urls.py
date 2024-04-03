from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Application Rest API",
        default_version='v1',
        description="Application Rest API",
        contact=openapi.Contact(email="rmehrojbek0797@gmail.com"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
        ),

    # path(
    #     'api/v1/', 
    #     include('api.v1.main.urls'),
    #     ),
    
    path(
        'docs/', 
        schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'
        ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
