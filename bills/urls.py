import debug_toolbar
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from .users.views import UserApiView, signin
from .core.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
    path('accounts/login-auth/', signin),
    path('api-token-auth/', views.obtain_auth_token),
    path('accounts/', include('rest_registration.api.urls')),
    path('endpoint/', include('bills.billsapi.urls')),
    path('user/', UserApiView.as_view(), name='user_detail'),
    re_path(r"^.*$", IndexTemplateView.as_view(), name='index-view'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
