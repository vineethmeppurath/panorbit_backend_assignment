from django.contrib import admin
from django.urls import path, include

from panorbit_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('panorbit_app.urls')),
    path('', views.home),

]
