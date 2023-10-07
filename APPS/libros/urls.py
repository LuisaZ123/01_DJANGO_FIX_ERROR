from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter

router.register(r'', views.librosViewSet, basename='libro')

urlpatterns = [
]

urlpatterns = urlpatterns + router.urls