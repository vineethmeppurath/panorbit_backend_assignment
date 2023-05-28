from django.contrib import admin
from django.urls import path

from panorbit_app import views
from panorbit_app.views import SignUp
from django.urls import path, include
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Panorbit',
        default_version='v1',
        description='Panorbit Backend Assignment',
        contact=openapi.Contact(email='contact@example.com'),
    ),
    public=True,
)
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
