import debug_toolbar
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
    path('accounts/', include('rest_registration.api.urls')),
    path('', include('bills.billsapi.urls')),
    path('__debug__/', include(debug_toolbar.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
