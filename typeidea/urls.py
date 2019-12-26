# from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
# from django.conf.urls.static import static

from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, demo
)

from config.views import links
from config.custom_site import custom_site


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(),
        name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(),
        name='post-detail'),
    url(r'^links/$', links, name='links'),

    url(r'^search/$', SearchView.as_view(), name='search'),

    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),

    url(r'^demo/', demo, name='demo'),

    # url(r'^ckeditor/', include('ckeditor_uploader.urls'))

] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
