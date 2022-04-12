"""epiceventsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, ClientViewSet
from crm.views import ContractViewSet, EventViewSet
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'contracts', ContractViewSet, basename="contracts")
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'events', EventViewSet, basename='events')


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
