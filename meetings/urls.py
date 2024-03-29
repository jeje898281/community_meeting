from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendViewSet

router = DefaultRouter()
router.register(r'attendance', AttendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]