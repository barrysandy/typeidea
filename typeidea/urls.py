from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from typeideas.views import IndexView

from blog.views import post_list, post_detail
from config.views import links
from config.custom_site import custom_site

urlpatterns = [
    url(r'^$', post_list),
    url(r'^category/(?P<category_id>\d+)/$', post_list),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list),
    url(r'^post/(?P<post_id>\d+).html$', post_detail),
    url(r'^links/$', links),

    url(r'^$', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('admin_blog/', custom_site.urls),
]
