from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter 

from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
   openapi.Info(
      title="Comute",
      default_version='v1',
      description="This is a REST API for a Comute",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ayaraerick@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('',include('orders.urls')),
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.social.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

