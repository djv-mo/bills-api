from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillsViewSet

app_name = 'bills'

router = DefaultRouter()
router.register(r'bills', BillsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
