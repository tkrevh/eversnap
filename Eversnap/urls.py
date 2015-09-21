from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from tweetsalbum.models import Picture, TUser, Album
from rest_framework import routers
from tweetsalbum import views
import settings

router = routers.DefaultRouter()
router.register(r'api/pictures', views.PictureViewSet)
router.register(r'api/albums', views.AlbumViewSet)
router.register(r'api/tusers', views.TUserViewSet)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^pictures/$', ListView.as_view(model=Picture,)),
    (r'^favorites/$', 'tweetsalbum.views.favorites'),
    (r'^favorites/(?P<album>\w+)/$', 'tweetsalbum.views.favorites_by_album'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Examples:
    # url(r'^$', 'Eversnap.views.home', name='home'),
    # url(r'^Eversnap/', include('Eversnap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # REST API
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
)
