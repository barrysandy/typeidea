from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from typeideas.views import IndexView

from config.custom_site import custom_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_blog/', custom_site.urls),
    url(r'^$', IndexView.as_view(), name='index')
]
