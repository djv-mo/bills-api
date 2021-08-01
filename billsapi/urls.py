from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (BillsViewSet,
                    BillsItemsListCreateApiView,
                    BillsItemRUDApiView)

app_name = 'bills'

router = DefaultRouter()
router.register(r'bills', BillsViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('bills/<uuid:pk>/items/',
         BillsItemsListCreateApiView.as_view(),
         name='items-list'),

    path('items/<uuid:pk>/',
         BillsItemRUDApiView.as_view(),
         name='items-update'),

    ]
